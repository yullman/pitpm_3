from fastapi import FastAPI, Query


app = FastAPI()


@app.get("/items/")
async def read_items(
    q: str | None = Query(
        default=None,
        title="Title",
        description="Description",
        min_length=1,
        max_length=15,
    ),
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q - ": q})
    return results

