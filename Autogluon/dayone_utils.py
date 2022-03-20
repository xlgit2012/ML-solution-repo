import matplotlib.pyplot as plt
import matplotlib.image as img
import pandas as pd
import os
import os.path
from os import path
from IPython.core.display import display, HTML
import codecs

def selected_option(message):
    # reading png image file
    im = img.imread("./messages/"+ message + ".png")
    # show image
    #plt.imshow(im,  aspect='auto')
    fig, ax = plt.subplots(figsize=(15, 15))
    plt.axis('off')
    ax.imshow(im)
    #tight_layout()
######################################
def mlu_answer(message):
    # reading csv answer file
    df = pd.read_csv("./messages/"+ message + ".csv")
    return df
######################################
def answer_html(message):
    f=codecs.open("./messages/"+ message + ".html", 'r')
    if (message == "BP1"):
        os.system("touch ./choices/BP1")
        if path.exists("./choices/BP2"):
            os.remove("./choices/BP2")
    else:
        os.system("touch ./choices/BP2")
        if path.exists("./choices/BP1"):
            os.remove("./choices/BP1")
    display(HTML(f.read()))
    return