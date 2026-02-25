from pydantic import BaseModel, Field

class ReportRequest(BaseModel):
    topic: str = Field(..., description="The topic for which the report is to be generated.")
    max_analysts: int = Field(3, description="The no. of analyst personas to create.")
    
class FeedbackRequest(BaseModel):
    thread_id: str
    feedback: str = ""
    
class LoginRequest(BaseModel):
    username: str = Field(..., description="The username for login.")
    password: str = Field(..., description="The password for login.")
    
class SignupRequest(BaseModel):
    username: str = Field(..., description="The desired username for signup.")
    password: str = Field(..., description="The desired password for signup.")

class ReportRequest(BaseModel):
    topic: str = Field(..., description="The topic for which the report is to be generated.")
    feedback: str | None = Field(None, description = "Optional feedback from analyst.")