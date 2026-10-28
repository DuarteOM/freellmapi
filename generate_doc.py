import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def create_report():
    doc = Document()

    # Page setup - Margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Helper function for adding headings with styling
    def add_custom_heading(text, level):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        if level == 1:
            run.font.name = 'Arial'
            run.font.size = Pt(18)
            run.font.color.rgb = RGBColor(24, 43, 73) # Deep Navy
        elif level == 2:
            run.font.name = 'Arial'
            run.font.size = Pt(14)
            run.font.color.rgb = RGBColor(41, 128, 185) # Accent Blue
        return p

    # Helper function for body text
    def add_custom_paragraph(text, bold_prefix=None, space_after=6):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_bold = p.add_run(bold_prefix)
            r_bold.bold = True
            r_bold.font.name = 'Calibri'
            r_bold.font.size = Pt(11)
            r_bold.font.color.rgb = RGBColor(51, 51, 51)
        r_text = p.add_run(text)
        r_text.font.name = 'Calibri'
        r_text.font.size = Pt(11)
        r_text.font.color.rgb = RGBColor(51, 51, 51)
        return p

    # Helper for adding image securely
    def add_image_safely(img_filename, caption_text):
        img_path = os.path.join(r"C:\Users\Utilizador\Pictures\Screenshots", img_filename)
        if os.path.exists(img_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(6)
            p_img.paragraph_format.space_after = Pt(2)
            run = p_img.add_run()
            run.add_picture(img_path, width=Inches(6.0))

            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_after = Pt(12)
            r_cap = p_cap.add_run(f"Figura: {caption_text}")
            r_cap.font.name = 'Calibri'
            r_cap.font.size = Pt(9.5)
            r_cap.font.italic = True
            r_cap.font.color.rgb = RGBColor(100, 100, 100)
        else:
            add_custom_paragraph(f"[Nota: Imagem '{img_filename}' não encontrada no caminho esperado.]", bold_prefix="Aviso: ")

    # 1. Capa Formal
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_p.paragraph_format.space_before = Pt(120)
    title_p.paragraph_format.space_after = Pt(12)
    r_title = title_p.add_run("Atividade 4 - Programação Imperativa I")
    r_title.bold = True
    r_title.font.name = 'Arial'
    r_title.font.size = Pt(24)
    r_title.font.color.rgb = RGBColor(24, 43, 73)

    sub_p = doc.add_paragraph()
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub_p.paragraph_format.space_after = Pt(180)
    r_sub = sub_p.add_run("Unidade Curricular de Engenharia Informática")
    r_sub.font.name = 'Arial'
    r_sub.font.size = Pt(14)
    r_sub.font.color.rgb = RGBColor(100, 110, 120)

    auth_p = doc.add_paragraph()
    auth_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    auth_p.paragraph_format.space_after = Pt(0)
    r_auth_label = auth_p.add_run("Trabalho realizado por:\n")
    r_auth_label.font.name = 'Calibri'
    r_auth_label.font.size = Pt(11)
    r_auth_label.font.color.rgb = RGBColor(100, 100, 100)

    r_auth = auth_p.add_run("Duarte OM e Afonso")
    r_auth.bold = True
    r_auth.font.name = 'Arial'
    r_auth.font.size = Pt(16)
    r_auth.font.color.rgb = RGBColor(41, 128, 185)

    doc.add_page_break()

    # --- Exercício 1 ---
    add_custom_heading("Exercício 1 - Declaração e inicialização", level=1)
    add_custom_paragraph("Declaração das variáveis primitivas (idade, altura, inicial, saldo) e impressão formatada no terminal no formato exigido.", bold_prefix="Resposta / Enunciado: ")
    add_image_safely("Captura de ecrã 2026-10-22 163231.png", "Execução do Exercício 1 - Declaração e inicialização de variáveis.")

    # --- Exercício 2 ---
    add_custom_heading("Exercício 2 - Correção de especificadores de formato", level=1)
    add_custom_paragraph("Análise e correção dos especificadores de formato em C.", bold_prefix="Enunciado: ")
    add_custom_paragraph("Os especificadores originais (%f %d %d %c) produziam valores incorretos e corrompidos porque existia um desalinhamento estrito entre os tipos dos argumentos passados para a função printf e os especificadores de formato interpretados. Em C, funções variádicas como o printf esperam que o tamanho em bytes na stack corresponda exatamente ao especificador (%d espera 4 bytes para int, %lf ou %f espera 8 bytes para double, %c espera char). Quando há discrepâncias, o motor de runtime lê fatias incorretas de bytes da stack, resultando em lixo de memória ou valores desfasados.", bold_prefix="Resposta Teórica Detalhada: ")
    add_image_safely("Captura de ecrã 2026-10-22 155439.png", "Execução do Exercício 2 - Correção de especificadores de formato.")

    # --- Exercício 3 ---
    add_custom_heading("Exercício 3 – Divisão inteira e real: previsão e verificação", level=1)
    add_custom_paragraph("Estudo do comportamento da divisão em C entre inteiros e reais, analisando as previsões e verificações.", bold_prefix="Enunciado: ")
    add_custom_paragraph("• Previsão Alínea a (17 / 2): Produz o valor 8, pois trata-se de uma divisão estritamente inteira (truncagem da parte fracionária).\n• Previsão Alínea b (17 / 2.0): Produz o valor 8.5, dado que o literal 2.0 é do tipo double, forçando a promoção implícita do operando inteiro para real antes da divisão.\n• Previsão Alínea c ((double)17 / 2): Produz o valor 8.5 devido ao cast explícito (double) que converte o numerador para real, garantindo a divisão em ponto flutuante.", bold_prefix="Resposta Teórica Detalhada: ")
    add_image_safely("Captura de ecrã 2026-10-22 155719.png", "Execução do Exercício 3 - Divisão inteira e real.")

    # --- Exercício 4 ---
    add_custom_heading("Exercício 4 - Eliminação de números mágicos", level=1)
    add_custom_paragraph("Substituição de constantes literais por identificadores significativos utilizando #define e const.", bold_prefix="Enunciado: ")
    add_custom_paragraph("• Diretiva #define: É uma macro processada pelo pré-processador antes da compilação. Realiza uma substituição textual literal em todo o código-fonte, não possui tipo associado e não ocupa espaço de memória RAM.\n• Qualificador const: É processado pelo compilador, possui tipo estrito e aloca espaço de armazenamento em memória.\n• Alteração de valor: Em ambos os casos, tentar reatribuir um novo valor gera erro de compilação.", bold_prefix="Resposta Teórica Detalhada: ")
    add_image_safely("Captura de ecrã 2026-10-22 160356.png", "Execução do Exercício 4 - Eliminação de números mágicos (#define vs const).")

    # --- Exercício 5 ---
    add_custom_heading("Exercício 5 - Inventário de tipos com sizeof", level=1)
    add_custom_paragraph("Medição do tamanho em bytes dos tipos fundamentais da linguagem C utilizando o operador sizeof.", bold_prefix="Enunciado: ")
    add_custom_paragraph("O padrão oficial da linguagem C garante apenas tamanhos mínimos e relações de ordem entre os tipos primitivos (sizeof(char) == 1 e short <= int <= long). O tamanho do tipo 'long' varia consoante a arquitetura (4 bytes em Windows x64 [LLP64] vs 8 bytes em Linux/macOS x64 [LP64]) para permitir otimização nativa do processador.", bold_prefix="Resposta Teórica Detalhada: ")
    add_image_safely("Captura de ecrã 2026-10-22 161510.png", "Execução do Exercício 5 - Inventário de tipos com sizeof.")

    # --- Exercício 6 ---
    add_custom_heading("Exercício 6 - Carateres e códigos ASCII", level=1)
    add_custom_paragraph("Manipulação de carateres, leitura segura com espaço e análise da tabela ASCII nos extremos alfabéticos e numéricos.", bold_prefix="Enunciado: ")
    add_custom_paragraph("• O espaço em ' %c' na função scanf instrui o motor de leitura a ignorar espaços em branco e newlines ('\\n') pendentes no buffer de entrada.\n• Nos extremos da tabela ASCII ('Z' código 90 e '9' código 57), a tabela prossegue sequencialmente: o caráter seguinte a 'Z' é '[' (ASCII 91) e o seguinte a '9' é ':' (ASCII 58), deixando de ser letras ou dígitos.", bold_prefix="Resposta Teórica Detalhada: ")
    add_image_safely("Captura de ecrã 2026-10-22 161613.png", "Exercício 6 - Teste de carateres e códigos ASCII (Teste para 'A').")
    add_image_safely("Captura de ecrã 2026-10-22 163839.png", "Exercício 6 - Teste de carateres e códigos ASCII (Teste para 'Z').")

    # --- Exercício 7 ---
    add_custom_heading("Exercício 7 - Troca de valores entre variáveis", level=1)
    add_custom_paragraph("Análise da troca de valores entre variáveis sem recurso a variável temporária.", bold_prefix="Enunciado: ")
    add_custom_paragraph("A sequência 'a = b; b = a;' falha porque a primeira instrução sobrepõe o valor de 'a' com o valor de 'b'. Na instrução seguinte, 'b' recebe o novo valor de 'a' (que já foi alterado), terminando ambas as variáveis com o mesmo valor final. É indispensável o uso de uma variável temporária.", bold_prefix="Resposta Teórica Detalhada: ")
    add_image_safely("Captura de ecrã 2026-10-22 161759.png", "Execução do Exercício 7 - Troca de valores entre variáveis.")

    # --- Exercício 8 ---
    add_custom_heading("Exercício 8 - Média por três caminhos", level=1)
    add_custom_paragraph("Comparação de três métodos para o cálculo da média aritmética em C.", bold_prefix="Enunciado: ")
    add_custom_paragraph("• m1: Divisão inteira truncada (33 / 2 = 16.00) - incorreta.\n• m2: Promoção por literal real 2.0 (16.50) - correta.\n• m3: Cast explícito da soma para double (16.50) - correta.", bold_prefix="Resposta Teórica Detalhada: ")
    add_image_safely("Captura de ecrã 2026-10-22 161900.png", "Execução do Exercício 8 - Média por três caminhos.")

    # --- Exercício 9 ---
    add_custom_heading("Exercício 9 - Conversor de moedas com ida e volta", level=1)
    add_custom_paragraph("Conversão bidirecional de moedas e análise de precisão numérica em vírgula flutuante.", bold_prefix="Enunciado: ")
    add_custom_paragraph("A representação em binário de vírgula flutuante (padrão IEEE 754) pode introduzir pequenas imprecisões. O especificador %.2f apenas formata a exibição visual no ecrã, enquanto em memória a variável mantém a precisão total do tipo double.", bold_prefix="Resposta Teórica Detalhada: ")
    add_image_safely("Captura de ecrã 2026-10-22 162113.png", "Execução do Exercício 9 - Conversor de moedas com ida e volta.")

    # --- Exercício 10 ---
    add_custom_heading("Exercício 10 – Relatório de estudante (integrador)", level=1)
    add_custom_paragraph("Emissão de relatório de estudante integrando constantes, cálculo de média sem truncagem e sizeof.", bold_prefix="Enunciado / Resposta: ")
    add_image_safely("Captura de ecrã 2026-10-22 162417.png", "Exercício 10 - Código e leitura de dados do estudante.")
    add_image_safely("Captura de ecrã 2026-10-22 162838.png", "Exercício 10 - Execução e relatório final integrador.")

    # Save document
    output_path = "Atividade_4_PI1_Atualizada.docx"
    doc.save(output_path)
    print(f"Document updated successfully at: {output_path}")

if __name__ == "__main__":
    create_report()
