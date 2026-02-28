from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status

from app.database import supabase
from app.middleware.auth import get_current_user
from app.models.orders import CheckoutRequest, OrderDetailResponse, OrderResponse

router = APIRouter()


@router.post("/checkout", response_model=OrderResponse)
async def checkout(
    checkout: CheckoutRequest, current_user: dict = Depends(get_current_user)
):
    """
    Create order and initiate payment.
    Requires authentication.

    Note: BCEL payment integration is placeholder for now.
    """
    try:
        # Create order
        order_data = {
            "user_id": current_user["id"],
            "total_amount": 0,  # Will calculate below
            "payment_method": checkout.payment_method.value,
            "payment_status": "pending",
            "order_number": f"ORD-{datetime.now().strftime('%Y%m%d')}-000001",  # Simplified
        }

        # Calculate total and create order items
        total_amount = 0
        items_data = []

        for item in checkout.items:
            # Get book price
            book_response = (
                supabase.table("books")
                .select("price_lak, rental_price_lak")
                .eq("id", item.book_id)
                .execute()
            )

            if not book_response.data:
                raise HTTPException(
                    status_code=404, detail=f"Book {item.book_id} not found"
                )

            book = book_response.data[0]

            # Determine price based on purchase type
            if item.purchase_type.value == "rental":
                price = book.get("rental_price_lak") or book["price_lak"] * 0.5
            else:
                price = book["price_lak"]

            # Calculate royalty (70% by default)
            royalty = price * 0.7

            total_amount += price
            items_data.append(
                {
                    "book_id": item.book_id,
                    "price_at_purchase": price,
                    "royalty_amount": royalty,
                    "purchase_type": item.purchase_type.value,
                }
            )

        # Update order total
        order_data["total_amount"] = total_amount

        # Insert order
        order_result = supabase.table("orders").insert(order_data).execute()
        order_id = order_result.data[0]["id"]

        # Insert order items
        for item_data in items_data:
            item_data["order_id"] = order_id
            supabase.table("order_items").insert(item_data).execute()

        # Return order response
        return {
            "id": order_id,
            "order_number": order_data["order_number"],
            "total_amount": total_amount,
            "payment_status": "pending",
            "payment_method": checkout.payment_method.value,
            "items_count": len(items_data),
            "created_at": datetime.now(),
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.get("", response_model=list)
async def list_orders(current_user: dict = Depends(get_current_user)):
    """
    List user orders.
    Requires authentication.
    """
    result = (
        supabase.table("orders")
        .select("*")
        .eq("user_id", current_user["id"])
        .order("created_at", desc=True)
        .execute()
    )
    return result.data


@router.get("/{order_id}", response_model=OrderDetailResponse)
async def get_order(order_id: str, current_user: dict = Depends(get_current_user)):
    """
    Get order details.
    Requires authentication.
    """
    # Get order
    order_result = (
        supabase.table("orders")
        .select("*")
        .eq("id", order_id)
        .eq("user_id", current_user["id"])
        .execute()
    )

    if not order_result.data:
        raise HTTPException(status_code=404, detail="Order not found")

    order = order_result.data[0]

    # Get order items
    items_result = (
        supabase.table("order_items").select("*").eq("order_id", order_id).execute()
    )

    return {
        "id": order["id"],
        "order_number": order["order_number"],
        "total_amount": order["total_amount"],
        "discount_amount": order.get("discount_amount", 0),
        "final_amount": order["total_amount"],
        "payment_status": order["payment_status"],
        "payment_method": order["payment_method"],
        "bcel_transaction_id": order.get("bcel_transaction_id"),
        "items": items_result.data,
        "created_at": order["created_at"],
    }
