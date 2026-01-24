import configparser
import glob
import json
import os
import re
import shutil
import smtplib
import sqlite3
import subprocess
import sys
import zipfile
from dotenv import load_dotenv
from datetime import datetime, timedelta
from email import encoders
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from io import StringIO
from time import sleep
import inspect
from typing import Any, Callable
from pathlib import Path
import urllib
import urllib.parse

from google import genai


import pandas as pd
from bs4 import BeautifulSoup

# Para colorir saidas de log
from colorama import Fore, init
from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
)
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common import keys, options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from unidecode import unidecode

import subprocess
import sqlite3
import shutil
import smtplib

# Para colorir saidas de log
from colorama import Fore, init
init(autoreset=True) # Faz o reset automático da cor após o print

# Import necessários para mexer com a lib webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

import datetime
import locale
import logging
import sys
import time
from datetime import datetime

import requests

# Import necessários para mexer com a lib webdriver-manager
from selenium import webdriver

# Para tratamento de erros
from selenium.common.exceptions import (
    NoSuchAttributeException,
    NoSuchElementException,
    NoSuchFrameException,
    NoSuchWindowException,
    StaleElementReferenceException,
    TimeoutException,
    WebDriverException,
)
from selenium.common.exceptions import (NoSuchAttributeException,
                                        NoSuchElementException,
                                        NoSuchFrameException,
                                        NoSuchWindowException,
                                        StaleElementReferenceException,
                                        TimeoutException, WebDriverException)

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common import keys, options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from unidecode import unidecode
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
