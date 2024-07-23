from flask import Blueprint, flash, redirect, render_template, request, url_for

from models import db
from models.profissional.profissional import Professional
from models.equivalencias.equivalence import Equivalence

prof = Blueprint('main', __name__, template_folder="views")

@prof.route('/verify/<int:professional_id>', methods=['GET', 'POST'])
def verify(professional_id):
    #tenta achar o engenheiro em questão no bd
    professional = Professional.query.get_or_404(professional_id)
    if request.method == 'POST':
        #pega o estado de destino
        state_to = request.form['state_to']
        missing_equivalences = []

        for attribute in professional.attributes:
            code_from = attribute.code
            #verifica se há a equivalência já no bd do código
            equivalence = Equivalence.query.filter_by(state_from=professional.state, state_to=state_to, code_from=code_from).first()
            if equivalence is None:
                missing_equivalences.append(code_from)

        if missing_equivalences:
            flash(f"Os seguintes códigos não têm equivalências para o estado {state_to}: {', '.join(missing_equivalences)}")
        else:
            flash('Todas as equivalências foram verificadas com sucesso.')
        
        return redirect(url_for('main.index'))
    return render_template('verify.html', professional=professional)
