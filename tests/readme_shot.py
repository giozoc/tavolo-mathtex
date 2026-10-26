import asyncio, sys
from playwright.async_api import async_playwright
from harness import open_app
async def main():
    async with async_playwright() as p:
        b, pg, errors = await open_app(p, width=1440, height=820)
        await pg.evaluate("t=>setSource(t)", "% Serie di Taylor centrata in x_0\nf(x) = \\sum_{n=0}^{\\infty}\n       \\frac{f^{(n)}(x_0)}{n!}\\,(x - x_0)^n")
        await pg.wait_for_timeout(900); await pg.click('#mf'); await pg.evaluate("()=>{ const m=MF.el; m.position=m.lastOffset; for (let k=0;k<7;k++) m.executeCommand('extendSelectionBackward'); }")
        await pg.wait_for_timeout(500)
        await pg.screenshot(path=sys.argv[1])
        print(errors); await b.close()
asyncio.run(main())
