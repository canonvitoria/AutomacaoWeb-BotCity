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

        if not self.find( "Lupa", matching=0.97, waiting_time=10000):
            self.not_found("Lupa")
        self.click()

        self.paste("cotaçao dolar")
        self.enter()

        if not self.find( "Dolar Americano", matching=0.97, waiting_time=10000):
            self.not_found("Dolar Americano")
        self.double_click_relative(26, 46)
        self.control_c()
        cotacao = self.get_clipboard()
        print(cotacao)
        
        if not self.find( "X", matching=0.97, waiting_time=10000):
            self.not_found("X")
        self.click()
        
        self.paste("cotaçao euro")
        self.enter()
        
        if not self.find( "euro", matching=0.97, waiting_time=10000):
            self.not_found("euro")
        self.double_click_relative(29, 47)
        self.control_c()
        cotacao = self.get_clipboard()
        print(cotacao)

        # Wait for 10 seconds before closing
        #self.wait(10000)

        # Stop the browser and clean up
        self.stop_browser()

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
