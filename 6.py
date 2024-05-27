from fastapi import FastAPI, Path, Query
app = FastAPI()


@app.get("/items/{i_id}")
async def read_items(
    *,
    item_id: int = Path(title="title", ge=0, le=100),
    q: str,
    size: int = Query(gt=0, lt=10),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

