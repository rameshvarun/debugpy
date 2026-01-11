import debugpy
import os

os.environ["DEBUGPY_LOG_DIR"] = "./logs"
os.environ["DEBUGPY_ADAPTER_ENDPOINTS"] = "./logs/endpoints.json"
debugpy.listen("unix://./debug.sock")
debugpy.wait_for_client()