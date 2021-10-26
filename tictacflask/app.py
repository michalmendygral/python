from flask import Flask, render_template, request

app = Flask(__name__)

cross = True
print('krzyz po deklaracji ', cross)

buttons = {'btn1': '',
           'btn2': '',
           'btn3': '',
           'btn4': '',
           'btn5': '',
           'btn6': '',
           'btn7': '',
           'btn8': '',
           'btn9': ''}

def sprawdz():
    wygrana = True
    if (buttons['btn1'] == buttons['btn2'] and  buttons['btn2'] == buttons['btn3'] and buttons['btn2'] != '' ):
        return wygrana
    if (buttons['btn4'] == buttons['btn5'] and  buttons['btn5'] == buttons['btn6'] and buttons['btn5'] != '' ):
        return wygrana
    if (buttons['btn7'] == buttons['btn8'] and  buttons['btn8'] == buttons['btn9'] and buttons['btn8'] != '' ):
        return wygrana
    if (buttons['btn1'] == buttons['btn4'] and  buttons['btn4'] == buttons['btn7'] and buttons['btn4'] != '' ):
        return wygrana
    if (buttons['btn2'] == buttons['btn5'] and  buttons['btn5'] == buttons['btn8'] and buttons['btn5'] != '' ):
        return wygrana
    if (buttons['btn3'] == buttons['btn6'] and  buttons['btn6'] == buttons['btn9'] and buttons['btn6'] != '' ):
        return wygrana
    if (buttons['btn1'] == buttons['btn5'] and  buttons['btn5'] == buttons['btn9'] and buttons['btn5'] != '' ):
        return wygrana
    if (buttons['btn3'] == buttons['btn5'] and  buttons['btn5'] == buttons['btn7'] and buttons['btn5'] != '' ):
        return wygrana

@app.route("/", methods=['GET', 'POST'])
def index():
    #btn1, btn2, btn3 = request.form.get('btn1'), request.form.get('btn2'), request.form.get('btn3')

    if request.method == 'POST':
        for key in buttons:
            #print('request.form.get(key) = ',request.form.get(key))
            if request.form.get(key) == '':
                global cross
                val = request.form.get(key)
                if val == '' and cross == True:
                    buttons[key] = 'X'
                elif val == '' and cross == False:
                    buttons[key] = 'O'
                cross = not cross
        else:
            # pass # unknown
            print("jestem w else")
        wygrana = sprawdz()
        my_string = 'krzyzyk' if cross == True else 'kolko'
        if wygrana == True:
            my_string = "Wygrywa " + 'krzyzyk' if (not cross) == True else 'kolko'
            for key in buttons:
                buttons[key] = ''

            #return render_template("game.html", btn1=buttons[btn1], btn2=buttons[btn2], btn3=buttons[btn3], my_string='Whats up?')
        return render_template("game.html", btn1=buttons['btn1'], btn2=buttons['btn2'], btn3=buttons['btn3'], btn4=buttons['btn4'],btn5=buttons['btn5'],
                               btn6=buttons['btn6'], btn7=buttons['btn7'], btn8=buttons['btn8'], btn9=buttons['btn9'], my_string= my_string )

    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")
        return render_template("game.html")

if __name__ == '__main__':
    app.run()