from fastapi import APIRouter, Depends, HTTPException, status
from app.middleware.auth import get_current_user
from app.models.users import UserRegister, UserLogin, DeviceRegister, UserProfile, DeviceInfo
from app.database import supabase

router = APIRouter()

@router.post("/me", response_model=UserProfile)
async def get_current_user_profile(current_user: dict = Depends(get_current_user)):
    """
    Get current user profile.
    Requires authentication.
    """
    return current_user

@router.post("/devices/register", response_model=DeviceInfo)
async def register_device(
    device: DeviceRegister,
    current_user: dict = Depends(get_current_user)
):
    """
    Register device for DRM (max 3 devices per user).
    Requires authentication.
    """
    try:
        # Check device limit
        existing_devices = supabase.table("user_devices").select("id").eq("user_id", current_user["id"]).execute()
        
        if len(existing_devices.data) >= 3:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Device limit reached (max 3 devices)"
            )
        
        # Register device
        result = supabase.table("user_devices").insert({
            "user_id": current_user["id"],
            "device_fingerprint": device.device_fingerprint,
            "device_name": device.device_name,
            "device_type": device.device_type.value
        }).execute()
        
        return result.data[0]
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/devices", response_model=list)
async def list_devices(current_user: dict = Depends(get_current_user)):
    """
    List registered devices.
    Requires authentication.
    """
    result = supabase.table("user_devices").select("*").eq("user_id", current_user["id"]).execute()
    return result.data

@router.delete("/devices/{device_id}")
async def remove_device(
    device_id: str,
    current_user: dict = Depends(get_current_user)
):
    """
    Remove a registered device.
    Requires authentication.
    """
    result = supabase.table("user_devices").delete().eq("id", device_id).eq("user_id", current_user["id"]).execute()
    
    if not result.data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Device not found"
        )
    
    return {"message": "Device removed successfully"}
