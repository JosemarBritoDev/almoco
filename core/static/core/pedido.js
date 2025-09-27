document.addEventListener('DOMContentLoaded', function() {
  const quantidade = document.getElementById('id_quantidade');
  const valorUnitario = document.getElementById('id_valor_unitario');
  const valorTotal = document.getElementById('id_valor_total');
  const marmitex = document.getElementById('id_marmitex');

  function calculaTotal() {
    if (quantidade && valorUnitario && valorTotal) {
      let qtde = parseFloat(quantidade.value) || 0;
      let vu = parseFloat(valorUnitario.value) || 0;
      valorTotal.value = (qtde * vu).toFixed(2);
    }
  }

  if (quantidade) quantidade.addEventListener('input', calculaTotal);
  if (valorUnitario) valorUnitario.addEventListener('input', calculaTotal);

  // Atualiza valorUnitario ao trocar marmitex
  if (marmitex) {
    marmitex.addEventListener('change', function() {
      const selectedOption = marmitex.options[marmitex.selectedIndex];
      // O preço não está disponível no select, então precisa passar via atributo
      // Solução: já buscar do backend via AJAX (simplificado para admin).
      // Sugestão: Use um atributo data-preco no campo select via ModelAdmin, 
      // ou uma chamada AJAX que retorna o preço do marmitex selecionado.

      // Exemplo abaixo para AJAX (requer view extra no backend):
      const marmitexId = marmitex.value;
      fetch(`/core/get_marmitex_preco/${marmitexId}/`)  // Você precisa criar essa URL!
        .then(response => response.json())
        .then(data => {
          valorUnitario.value = data.preco;
          calculaTotal();
        });
    });
  }
});
