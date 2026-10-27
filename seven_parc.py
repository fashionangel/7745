import time
import os
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

class Parser:

    def __init__(self, link):
        self.link = link
        self.driver = webdriver.Chrome()
        self.driver.get(self.link)
        self.info_list = []
        self.links_list = [] 
        self.date_dict = {}

    # def tryis(self):
    #     clickable_element = WebDriverWait(self.driver, 2).until(
    #       EC.element_to_be_clickable((By.ID, "dldkdAccept"))
    #     )
    #     clickable_element.click()

    def accept_cookie(self):
        clickable_element = WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable((By.ID, "dldkdAccept"))
        )
        clickable_element.click()

    def electro_choice(self):
        clickable_element = WebDriverWait(self.driver, 5).until(  #min-h-[54px]    
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div[5]/div/div/main/div[2]/div[2]/aside/div[1]/form/div[5]/div[2]/div[2]/label"))
        )
        self.driver.execute_script("arguments[0].click();", clickable_element)

    def power(self):
        clickable_element = WebDriverWait(self.driver, 5).until(  #min-h-[54px]    
            EC.element_to_be_clickable((By.XPATH, "//*[@id='catalog-filter-form']/div[7]/div[2]/div[1]/label/span[1]/span"))
        )
        clickable_element.click()

    def power_second(self):
        clickable_element = WebDriverWait(self.driver, 3).until(  #min-h-[54px]    
           EC.element_to_be_clickable((By.XPATH, "//*[@id='catalog-filter-form']/div[7]/div[2]/div[2]/label/span[1]/span"))
        )
        clickable_element.click()

    def mange(self):
        clickable_element = WebDriverWait(self.driver, 3).until(  #min-h-[54px]    
            EC.element_to_be_clickable((By.XPATH, "//*[@id='catalog-filter-form']/div[12]/div[2]/div[9]/label/span[1]/span"))
        )
        self.driver.execute_script("arguments[0].click();", clickable_element)

    def show_product(self):
        clickable_element = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='catalog-filter-form']/div[22]/button[1]"))
        )
        clickable_element.click()

    def get_links_page(self):
        elements = self.driver.find_elements(By.CLASS_NAME, 'c-list__center')
        for element in elements:
            link = element.find_element(By.TAG_NAME, 'a')
            self.links_list.append(link.get_attribute('href'))
    

    


    def go_to_the_next_page(self):
        # Заглушка для go_to_the_next_page
        pass

    def get_info(self):
        # Заглушка для get_info
        pass

    def creating_csv_file(self):
        # Заглушка для creating_csv_file
        pass





