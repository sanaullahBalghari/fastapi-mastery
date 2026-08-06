from fastapi import Request
import time


async def log_requests(request: Request, call_next):

    print("\n" + "=" * 50)
    print("📥 Incoming Request")
    print(f"Method : {request.method}")
    print(f"Path   : {request.url.path}")

    start_time = time.time()

    # Request ko Route tak bhejna
    response = await call_next(request)

    end_time = time.time()

    print("📤 Response Sent")
    print(f"Status Code : {response.status_code}")
    print(f"Execution Time : {end_time - start_time:.4f} sec")
    print("=" * 50)

    return response