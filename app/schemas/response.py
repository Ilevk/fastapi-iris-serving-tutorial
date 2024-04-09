from pydantic import BaseModel, Field


class IrisResp(BaseModel):
    target: int = Field(..., example=0, description="Predicted class")


class ResponseModel(BaseModel):
    status_code: int = Field(..., example=200, description="Status code")
    data: IrisResp = Field(..., description="Response data")
