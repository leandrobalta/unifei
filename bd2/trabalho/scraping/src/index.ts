import * as puppeteer from 'puppeteer'


async function main() {
    const browser = await puppeteer.launch({ headless: false })
    const page = await browser.newPage()
    await page.goto('https://www.linkedin.com/in/adamjposner/')

    await page.waitForSelector("#experience");

    await page.evaluate(() => {
        const name = document.querySelector('#ember38 h1')?.innerHTML
        console.log(name)
    })

    await browser.close()
}

main()