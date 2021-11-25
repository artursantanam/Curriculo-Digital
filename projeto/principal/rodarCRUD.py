O código abaixo seria adaptado para o site, porém eu não tive tempo de implementar :/



from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
 return render_template('CRUD.html')

@app.route('/incluir', methods=['POST'])
def incluir():

 nme = request.form['nme']
 dose1 = request.form['dose1']
 dose2 = request.form['dose2']
 total = request.form['total']

 mysql = bd.SQL("root", "", "test")
 comando = "INSERT INTO tb_vac(nme_pais, tot_vac_uma_dose, tot_vac_duas_doses, tot_populacao) VALUES (%s, %s, %s, %s);"
 if mysql.executar(comando, [nme, dose1, dose2, total]):
     msg="País " + nme + " cadastrado com sucesso!"
 else:
     msg="Falha na inclusão de País."

 return msg

@app.route('/buscar', methods=['POST'])
def buscar():

 parte = request.form['parte']

 mysql = bd.SQL("root", "", "test")
 comando = "SELECT * FROM tb_vac WHERE nme_pais LIKE CONCAT('%', %s, '%') ORDER BY nme_pais;"
 cs=mysql.consultar(comando, [parte])
 print(cs)
 dados = cs.fetchone()
 if dados == None:
     saida = ""
 else:
     saida = str(dados[0]) + ',' + dados[1] + ',' + str(dados[2]) + ',' + str(dados[3]) + ',' + str(dados[4])

 return saida


@app.route('/alterar', methods=['POST'])
def alterar():

 # Recuperando dados vindos do Ajax
 idt = request.form['idt']
 nme = request.form['nme']
 dose1 = request.form['dose1']
 dose2 = request.form['dose2']
 total = request.form['total']

 mysql = bd.SQL("root", "", "test")
 comando = "UPDATE tb_vac SET nme_pais=%s, tot_vac_uma_dose=%s, tot_vac_duas_doses=%s, tot_populacao=%s WHERE idt_vac=%s;"
 if mysql.executar(comando, [nme, dose1, dose2, total, idt]):
     msg="País " + nme + " alterada com sucesso!"
 else:
     msg="Falha na alteração de país."

 return msg


@app.route('/excluir', methods=['POST'])
def excluir():

 idt = request.form['idt']
 nme = request.form['nme']

 mysql = bd.SQL("root", "", "test")
 comando = "DELETE FROM tb_vac WHERE idt_vac=%s;"
 if mysql.executar(comando, [idt]):
     msg="País " + nme + " excluida com sucesso!"
 else:
     msg="Falha na exclusão de país."

 return msg


app.run()
