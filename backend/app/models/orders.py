from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime, date
from enum import Enum

class PaymentMethod(str, Enum):
    """Payment method enum"""
    BCEL_ONE = "bcel_one"
    BANK_TRANSFER = "bank_transfer"
    TELECOM = "telecom"
    CREDIT = "credit"

class PaymentStatus(str, Enum):
    """Payment status enum"""
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"

class PurchaseType(str, Enum):
    """Purchase type enum"""
    PURCHASE = "purchase"
    RENTAL = "rental"

class CheckoutItem(BaseModel):
    """Checkout item request"""
    book_id: str
    purchase_type: PurchaseType = PurchaseType.PURCHASE

class CheckoutRequest(BaseModel):
    """Checkout request"""
    items: List[CheckoutItem]
    payment_method: PaymentMethod
    return_url: str

class OrderItemResponse(BaseModel):
    """Order item response"""
    id: str
    book_id: str
    price_at_purchase: float
    royalty_amount: float
    purchase_type: PurchaseType
    access_expires_at: Optional[datetime] = None

class OrderResponse(BaseModel):
    """Order response"""
    id: str
    order_number: str
    total_amount: float
    payment_status: PaymentStatus
    payment_method: PaymentMethod
    items_count: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class OrderDetailResponse(BaseModel):
    """Order detail response with items"""
    id: str
    order_number: str
    total_amount: float
    discount_amount: float
    final_amount: float
    payment_status: PaymentStatus
    payment_method: PaymentMethod
    bcel_transaction_id: Optional[str] = None
    items: List[OrderItemResponse]
    created_at: datetime
    
    class Config:
        from_attributes = True
