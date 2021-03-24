# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 12:38:39 2021

@author: moghe
"""
from pytube import YouTube
import os
import requests
import bs4
import webbrowser
import wikipedia
import pyautogui
import pyautogui as pg
import keyboard
import time
from sympy import *
import math
from math import gcd 
from functools import reduce
from fractions import Fraction
import pandas as pd
def set_variables(variables):
    return symbols(variables)
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z=set_variables(['a',
 'b',
 'c',
 'd',
 'e',
 'f',
 'g',
 'h',
 'i',
 'j',
 'k',
 'l',
 'm',
 'n',
 'o',
 'p',
 'q',
 'r',
 's',
 't',
 'u',
 'v',
 'w',
 'x',
 'y',
 'z'])
def solve_equation(equation,equals,variables):
    '''solve equations'''
    system = [
    Eq(equation, equals),
    ]
    soln = solve(system, variables)
    print(soln)
def get_lcm(number_list):
  '''find the lowest common factor with panclus'''  
  lcm = number_list[0]
  for i in range(1,len(number_list)):
    lcm =(lcm*number_list[i]//math.gcd(lcm, number_list[i]))
  print('{'+str(int(lcm))+'}')
def inf(a,b):
    '''find hcf/gcd of any 2 numbers'''
    if a==0:
        return b 
    else:
        return inf(b%a,a)
def get_hcf(number_list):
    '''get hcf of a list'''
    gcdp = reduce(lambda x,y:inf(x,y),number_list)
    print(gcdp)
def convert_to_fraction(decimal):
    '''convert a decimal to fraction'''
    fraction=str(Fraction(decimal))
    print(fraction)
def probablityof(favourable_outcomes, total_outcomes) : 
    '''find the probablity of an event'''
    if favourable_outcomes > total_outcomes:
        raise Exception('Favourable outcomes greater than total outcomes\n\nUnable to find probablity')
    else:
        d = gcd(favourable_outcomes, total_outcomes); 
        x = favourable_outcomes // d; 
        y = total_outcomes // d; 
        print('{'+str(x)+'/'+str(y)+'}'); 
def displaylowest(numerator,denominator):
    '''get any fraction in it's lowest form'''
    d = gcd(numerator, denominator); 
    x = numerator // d; 
    y = denominator // d; 
    print('{'+str(x)+'/'+str(y)+'}');
def roots(root,number):
    '''see the roots like fifth root of 125 of any other with this attribute'''
    rot=1/root
    new=number*rot
    print(new)
def solve_expr(expression):
    '''solve a algebraic expression'''
    try:print('{',expand(expression),'}')
    except:
        raise TypeError('Not able to solve the expression check your variable and try again')
def getFactor(expression):
    '''do factorization in python'''
    print(factor(expression))
def create_table(data,headings,indexes):
    '''create a table to arrange your data'''
    # Create the pandas DataFrame 
    df = pd.DataFrame(data, columns = headings,index=indexes) 
    print(df)
def download_from_youtube(url,path):
    '''download youtube videos to a path'''
    print('Downloading your request\n')
    import pytube  
    from pytube import YouTube  
    video_url = url  
    youtube = pytube.YouTube(video_url)  
    video = youtube.streams.first()  
    video.download(path)
    print('Your video is saved to',path)
def get_results(search_url,data,_class_):
    '''will scrape the results'''
    '''create example like get_results('https://www.google.com/search?q=','what is panclus','BNeawe')'''
    text= data
    url = search_url + text 
    request_result=requests.get( url ) 
    soup = bs4.BeautifulSoup(request_result.text, 
                             "html.parser") 
    temp = soup.find( "div" , class_=_class_ ).text
    print(temp)
def wikit_on(page):
    '''scrape wikipedia with python'''
    return wikipedia.summary(page)
def open_link(url):
    '''automating links and websites with open_link'''
    new=2;
    webbrowser.open(url,new)
def call_ip(website):
    '''call the ip address of your url'''
    import socket
    url=website
    print(socket.gethostbyname(url))
def inspect(address):
    '''inspect a address'''
    try:
        import requests
        req = requests.get(address)
        print(req.text)
    except:
        print('Unable to get the code please check your url')