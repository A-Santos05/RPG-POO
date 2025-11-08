from __future__ import annotations
from dataclasses import dataclass
from .personagem import Personagem
from .inimigo import Inimigo
import random

@dataclass
class ResultadoMissao:
    """Resultado ilustrativo (placeholder)."""
    venceu: bool = False
    detalhes: str = "Missão simulada."


class Missao:
    """
    Estrutura da missão sem a mecânica de combate.
    Mantém a assinatura para futura integração com o jogo completo.
    """

    def __init__(self, titulo: str, inimigo: Inimigo):
        self.titulo = titulo
        self.inimigo = inimigo

    def executar(self, p: Personagem) -> ResultadoMissao:
        """
        Execução da missão: Combate Turno-a-Turno Simples.
        """
        # Verifica se o personagem está pronto para lutar
        if not p.vivo:
            return ResultadoMissao(venceu=False, detalhes=f"{p.nome} está esgotado.")
        
        # --- Configuração Inicial ---
        
        # Re-cria o inimigo (opcional) para garantir que comece com HP cheio. 
        # Ou simplesmente garante que self.inimigo esteja com vida máxima.
        # Aqui, vamos assumir que self.inimigo é a instância para o combate.
        i = self.inimigo
        i._atrib.vida = i._atrib.vida_max # Garante HP cheio no início do combate
        
        print(f"\n=== Missão: {self.titulo} ===")
        print(f"O combate entre {p.nome} (Lvl {p.nivel}) e {i.nome} (HP: {i._atrib.vida}) começa!")

        # --- Loop Principal do Combate ---
        turno = 1
        while p.vivo and i.vivo:
            print(f"\n--- Turno {turno} ---")
            
            # 1. PERSONAGEM ATACA INIMIGO
            # Chamada ao método que você deve implementar em Personagem
            try:
                dano_personagem = p.calcular_dano_base() 
                
                # Chamada ao método de Entidade para cálculo de dano
                dano_recebido_inimigo = i.receber_dano(dano_personagem) 
                
                print(f"{p.nome} ataca! Dano base: {dano_personagem}.")
                print(f"{i.nome} recebe {dano_recebido_inimigo} de dano.")
                print(f"HP {i.nome}: {i.barra_hp(10)}")

            except NotImplementedError:
                print("ERRO: Implemente Personagem.calcular_dano_base() primeiro.")
                return ResultadoMissao(venceu=False, detalhes="Combate interrompido por erro de implementação.")


            if not i.vivo:
                print(f"\n🎉 {i.nome} foi derrotado!")
                break
                
            # 2. INIMIGO ATACA PERSONAGEM
            
            # Usamos o método 'atacar' da classe Entidade (método base simples)
            dano_inimigo = i.atacar()
            dano_recebido_personagem = p.receber_dano(dano_inimigo)
            
            print(f"{i.nome} revida! Dano base: {dano_inimigo}.")
            print(f"{p.nome} recebe {dano_recebido_personagem} de dano.")
            print(f"HP {p.nome}: {p.barra_hp(10)}")

            if not p.vivo:
                print(f"\n☠️ {p.nome} foi derrotado!")
                break
                
            turno += 1
            # Adicionar um pequeno delay ou pausa aqui se fosse um jogo real

        # --- Resultado Final ---
        if p.vivo:
            print(f"Vitória! {p.nome} concluiu a missão {self.titulo}.")
            # Lógica de XP/Recompensa aqui
            return ResultadoMissao(venceu=True, detalhes=f"{p.nome} derrotou {i.nome}.")
        else:
            print(f"Derrota! {p.nome} falhou na missão {self.titulo}.")
            return ResultadoMissao(venceu=False, detalhes=f"{p.nome} foi derrotado por {i.nome}.")
