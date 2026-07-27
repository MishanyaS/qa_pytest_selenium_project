from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage

class SliderPage(BasePage):
    SLIDER = (
        By.CSS_SELECTOR,
        "input[type='range']"
    )

    SLIDER_VALUE = (
        By.ID,
        "sliderValue"
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
                            
    def slider_visible(self) -> bool:
        return self.is_visible(self.SLIDER)

    def slider_value_visible(self) -> bool:
        return self.is_visible(self.SLIDER_VALUE)

    def slider_value(self) -> str | None:
        return self.attribute(self.SLIDER, "value")

    def slider_value_text(self) -> str:
        return self.text(self.SLIDER_VALUE)

    def slider_min(self) -> str | None:
        return self.attribute(self.SLIDER, "min")

    def slider_max(self) -> str | None:
        return self.attribute(self.SLIDER, "max")

    def slider_step(self) -> str | None:
        return self.attribute(self.SLIDER, "step")

    def set_slider_value(self, value: int) -> None:
        self.execute_script(
            """
            const slider = arguments[0];
            const value = arguments[1];

            const setter = Object.getOwnPropertyDescriptor(
                HTMLInputElement.prototype,
                'value'
            ).set;

            setter.call(slider, value);

            slider.dispatchEvent(
                new Event('input', { bubbles: true })
            );

            slider.dispatchEvent(
                new Event('change', { bubbles: true })
            );
            """,
            self.wait_visible(self.SLIDER),
            value
        )

    def increase_slider(self, steps: int = 1) -> None:
        slider = self.wait_visible(self.SLIDER)

        for _ in range(steps):
            slider.send_keys(Keys.ARROW_RIGHT)

    def decrease_slider(self, steps: int = 1) -> None:
        slider = self.wait_visible(self.SLIDER)
        
        for _ in range(steps):
            slider.send_keys(Keys.ARROW_LEFT)

    def set_slider_to_min(self) -> None:
        minimum = self.slider_min()

        if minimum is None:
            raise ValueError("Slider minimum value is not defined")

        self.set_slider_value(int(minimum))

    def set_slider_to_max(self) -> None:
        maximum = self.slider_max()

        if maximum is None:
            raise ValueError("Slider maximum value is not defined")

        self.set_slider_value(int(maximum))
    
