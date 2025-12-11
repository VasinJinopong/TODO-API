import structlog

"""สร้างฟังก์ชั่นการ log เพื่อใช้กับ unhandler exception, http exception"""

structlog.configure(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer()
    ]
)

logger = structlog.get_logger()


