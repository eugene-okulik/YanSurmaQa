from time import sleep
from playwright.sync_api import Page, expect, Route
import json


def test_title_after_route_response(page: Page):
    url = 'https://www.apple.com/shop/api/digital-mat?path=library/step0_iphone/digitalmat'

    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['productName'] = 'яблокофон 15 про'
        body['body']['digitalMat'][0]['familyTypes'][0]['tabTitle'] = 'яблокофон 15 про'
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )
    page.route(url, handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone')
    pop_up = page.locator('(//div[@class="rf-hcard-copy"])[1]')
    pop_up.hover()
    pop_up.click()
    title = page.locator('(//h2[@id="rf-digitalmat-overlay-label-0"])[1]')
    expect(title).to_have_text('iPhone 15 Pro')
    sleep(5)
