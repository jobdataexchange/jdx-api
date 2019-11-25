from pocha import describe, it, before, after
from expects import expect, equal, be_none, be, be_above, be_true
from ...pocha_setup import application


@describe('/health')
def _():

    @it("GET 200's")
    def _():
        resp = application.get('/health')

        expect(resp.status_int).to(equal(200))
