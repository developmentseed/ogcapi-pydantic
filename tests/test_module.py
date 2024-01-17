"""ogcapi-pydantic test."""

from ogcapi_pydantic import model


def test_link():
    """test link model."""
    link = model.Link(
        href="http://somewhere.over.the/rainbow.json",
        rel="data",
        type="application/json",
    )
    assert link.model_dump()
