import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

BaseDados = pd.read_csv('D:\\Python\\Teste_Kroton\\Teste_Kroton_Planilha2_Teste.2.csv', encoding='latin-1')
BaseDados_Sem_Ed = pd.read_csv('D:\\Python\\Teste_Kroton\\Teste_Kroton_Planilha2_Teste_SEM_ED.csv', encoding='latin-1')
BaseDados_Com_Ed = pd.read_csv('D:\\Python\\Teste_Kroton\\Teste_Kroton_Planilha2_Teste_COM_ED.csv', encoding='latin-1')

CSV_MédiaGeral_CE = BaseDados.groupby("nome_curso_padronizado").mean()["nt_ce"].sort_values()
CSV_MédiaGeral_CE_Sem_ED = BaseDados_Sem_Ed.groupby("nome_curso_padronizado").mean()["nt_ce"].sort_values()
CSV_MédiaGeral_CE_Com_ED = BaseDados_Com_Ed.groupby("nome_curso_padronizado").mean()["nt_ce"].sort_values()

CSV_MédiaGeral_FG = BaseDados.groupby("nome_curso_padronizado").mean()["nt_fg"].sort_values()
CSV_MédiaGeral_FG_Sem_ED = BaseDados_Sem_Ed.groupby("nome_curso_padronizado").mean()["nt_fg"].sort_values()
CSV_MédiaGeral_FG_Com_ED = BaseDados_Com_Ed.groupby("nome_curso_padronizado").mean()["nt_fg"].sort_values()

CSV_MédiaGeral = BaseDados.groupby("nome_curso_padronizado").mean()["nt_ger_tratado"].sort_values()
CSV_MédiaGeral_Sem_ED = BaseDados_Sem_Ed.groupby("nome_curso_padronizado").mean()["nt_ger_tratado"].sort_values()
CSV_MédiaGeral_Com_ED = BaseDados_Com_Ed.groupby("nome_curso_padronizado").mean()["nt_ger_tratado"].sort_values()

CSV_MédiaGeral_CE.to_csv('D:\\Python\\Teste_Kroton\\MédiaGeral_CE.csv', encoding='latin- 1', index=True)
CSV_MédiaGeral_CE_Sem_ED.to_csv('D:\\Python\\Teste_Kroton\\MédiaGeral_CE_Sem_Ed.csv', encoding='latin- 1', index=True)
CSV_MédiaGeral_CE_Com_ED.to_csv('D:\\Python\\Teste_Kroton\\Média_Geral_CE_Com_Ed.csv', encoding='latin- 1', index=True)

CSV_MédiaGeral_FG.to_csv('D:\\Python\\Teste_Kroton\\MédiaGeral_FG.csv', encoding='latin- 1', index=True)
CSV_MédiaGeral_FG_Sem_ED.to_csv('D:\\Python\\Teste_Kroton\\MédiaGeral_FG_Sem_Ed.csv', encoding='latin- 1', index=True)
CSV_MédiaGeral_FG_Com_ED.to_csv('D:\\Python\\Teste_Kroton\\Média_Geral_FG_Com_Ed.csv', encoding='latin- 1', index=True)

CSV_MédiaGeral.to_csv('D:\\Python\\Teste_Kroton\\MédiaGeral.csv', encoding='latin- 1', index=True)
CSV_MédiaGeral_Sem_ED.to_csv('D:\\Python\\Teste_Kroton\\MédiaGeral_Sem_Ed.csv', encoding='latin- 1', index=True)
CSV_MédiaGeral_Com_ED.to_csv('D:\\Python\\Teste_Kroton\\Média_Geral_Com_Ed.csv', encoding='latin- 1', index=True)


BaseDados.replace({'sim': 1}, regex=True, inplace=True) 
BaseDados.replace({'nao_encontrado': 0}, regex=True, inplace=True) 
BaseDados.replace({'nao': 0}, regex=True, inplace=True) 

print(BaseDados.corr())

print(BaseDados[['fez_ed','nt_ger_tratado','nt_fg','nt_ce','nota_mt','nota_lc','nota_ch','nota_cn','nota_rd']].corr('spearman'))
print(BaseDados[['fez_ed','nt_ger_tratado','nt_fg','nt_ce','nota_mt','nota_lc','nota_ch','nota_cn','nota_rd']].corr())
