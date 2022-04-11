from botcity.web import WebBot, Browser
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(WebBot):
    def action(self, execution=None):
        # Configure whether or not to run on headless mode
        self.headless = True

        # Uncomment to set the WebDriver path
        self.driver_path = "./chromedriver.exe"

        # Opens the BotCity website.
        self.browse("https://www.google.com")
        
        if not self.find( "lupa", matching=0.97, waiting_time=10000):
            self.not_found("lupa")
        self.click()
        
        self.paste("cotaçao dolar")
        self.enter()
        
        if not self.find( "dolaramericano", matching=0.97, waiting_time=10000):
            self.not_found("dolaramericano")
        self.double_click_relative(22, 50)
        self.control_c()
        cotacao_dolar = self.get_clipboard()
        
        if not self.find( "x", matching=0.97, waiting_time=10000):
            self.not_found("x")
        self.click()
        self.paste("cotaçao euro")
        self.enter()
        
        
        if not self.find( "euro", matching=0.97, waiting_time=10000):
            self.not_found("euro")
        self.double_click_relative(23, 51)
        
        self.control_c()
        cotacao_euro = self.get_clipboard()

        print(f"Dolar: {cotacao_dolar} Euro: {cotacao_euro}")

        # Wait for 10 seconds before closing
        # self.wait(10000)

        # Stop the browser and clean up
        self.stop_browser()

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
