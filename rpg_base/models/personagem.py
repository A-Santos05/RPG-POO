from __future__ import annotations
from .base import Entidade, Atributos
import random


class Personagem(Entidade):
    """
    Classe base única do jogador.
    Esta versão NÃO implementa a lógica principal de combate.
    """

    def __init__(self, nome: str, atrib: Atributos):
        super().__init__(nome, atrib)
        self.nivel = 1
        self.xp = 0

    def calcular_dano_base(self) -> int:
        """
        Implementação simples: Ataque base + aleatoriedade, ignorando crítico por enquanto.
        """
        # Vamos simular um dano que varia entre 80% e 120% do ATK base
        #dano_min = int(self._atrib.ataque * 0.8)
        #dano_max = int(self._atrib.ataque * 1.2)
        
        # O dano real que será usado como entrada para o 'receber_dano' do Inimigo
        #dano_base = random.randint(dano_min, dano_max)
        dano_base = self._atrib.ataque  # Implementação simplificada inicial
        return dano_base 

    def habilidade_especial(self) -> int:
        """
        Deve retornar dano especial (ou 0 se indisponível).
        (ex.: consumir self._atrib.mana e aplicar bônus de dano)
        """
        raise NotImplementedError("Implementar habilidade especial do Personagem.")
