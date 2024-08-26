//alert('O arquivo JS foi carregado com sucesso!');


// Função para formatar os campos como moeda brasileira
function formatarMoeda(elemento) {
  let valor = elemento.value;
  
  // Remove qualquer caractere que não seja dígito ou vírgula
  valor = valor.replace(/\D/g, "");
  
  // Formata como R$ XX.XXX,XX
  valor = (valor / 100).toFixed(2) + "";
  valor = valor.replace(".", ",");
  valor = valor.replace(/(\d)(?=(\d{3})+\,)/g, "$1.");
  
  // Adiciona o símbolo de moeda
  elemento.value = "R$ " + valor;
}

// Adiciona o evento de input aos campos saldo e limite_especial
document.getElementById('valor_deposito').addEventListener('input', function() {
  formatarMoeda(this);
});

document.getElementById('valor_saque').addEventListener('input', function() {
  formatarMoeda(this);
});

document.getElementById('valor_transferencia').addEventListener('input', function() {
  formatarMoeda(this);
});


// Mostra a data
document.addEventListener('DOMContentLoaded', function() {
  // Código para obter a data e hora mostrada na página
  const now = new Date();
  const dataFormatada = now.toLocaleDateString();
  const horaFormatada = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  document.getElementById('dataHora').textContent = `${dataFormatada} ${horaFormatada}`;
});


// Gerencia a exibição das operações de acordo com a seleção o select
document.addEventListener('DOMContentLoaded', function() {
  // Adiciona o evento para mudar o formulário ao selecionar uma operação
  document.getElementById('operacao').addEventListener('change', function() {
    // Esconde todos os campos
    document.getElementById('campo_deposito').style.display = 'none';
    document.getElementById('campo_saque').style.display = 'none';
    document.getElementById('campo_transferencia').style.display = 'none';

    // Mostra o campo correto com base na seleção
    var operacaoSelecionada = this.value;
    if (operacaoSelecionada === 'deposito') {
      document.getElementById('campo_deposito').style.display = 'block';
    } else if (operacaoSelecionada === 'saque') {
      document.getElementById('campo_saque').style.display = 'block';
    } else if (operacaoSelecionada === 'transferencia') {
      document.getElementById('campo_transferencia').style.display = 'block';
    }
  });

  // Inicializa a visibilidade dos campos com base na seleção inicial
  document.getElementById('operacao').dispatchEvent(new Event('change'));
});