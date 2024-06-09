from fastapi import APIRouter, HTTPException
from app.models.request_response import AdditionRequest, AdditionResponse
from app.controllers.addition_controller import addition_controller
import logging
import datetime

router = APIRouter()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/add", response_model=AdditionResponse)
async def add_numbers(request: AdditionRequest):
    logger.info("Received request: %s", request)
    try:
		
    	started_at = datetime.datetime.now()

    	batchid = request.batchid
    	results = addition_controller(request.payload)
    	status = "complete"
    	completed_at = datetime.datetime.now()
    	if None in results:
            raise ValueError("One of the lists could not be processed")
        
    	return AdditionResponse(batchid = batchid, response=results, status = status, started_at = started_at, completed_at = completed_at )
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail=str(e))
