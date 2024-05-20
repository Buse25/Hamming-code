import tkinter as tk
from tkinter import messagebox

def calculate_hamming_code(data):
    data = list(data)
    data.reverse()
    c, ch, j, r, h = 0, 0, 0, 0, []

    while ((len(data) + r + 1) > (pow(2, r))):
        r = r + 1

    for i in range(0, (r + len(data))):
        p = (2 ** c)

        if (p == (i + 1)):
            h.append(0)
            c = c + 1
        else:
            h.append(int(data[j]))
            j = j + 1

    for parity in range(0, (len(h))):
        ph = (2 ** ch)
        if (ph == (parity + 1)):
            start_index = ph - 1
            i = start_index
            to_xor = []

            while (i < len(h)):
                block = h[i:i + ph]
                to_xor.extend(block)
                i += 2 * ph

            for z in range(1, len(to_xor)):
                h[start_index] = h[start_index] ^ to_xor[z]
            ch += 1

    h.reverse()
    return ''.join(map(str, h))

def detect_and_correct_error(hamming_code):
    data = list(hamming_code)
    data.reverse()
    c, ch, j, r, error, h, parity_list, h_copy = 0, 0, 0, 0, 0, [], [], []

    for k in range(0, len(data)):
        p = (2 ** c)
        h.append(int(data[k]))
        h_copy.append(data[k])
        if (p == (k + 1)):
            c = c + 1

    for parity in range(0, (len(h))):
        ph = (2 ** ch)
        if (ph == (parity + 1)):
            start_index = ph - 1
            i = start_index
            to_xor = []

            while (i < len(h)):
                block = h[i:i + ph]
                to_xor.extend(block)
                i += 2 * ph

            for z in range(1, len(to_xor)):
                h[start_index] = h[start_index] ^ to_xor[z]
            parity_list.append(h[parity])
            ch += 1

    parity_list.reverse()
    error = sum(int(parity_list) * (2 ** i) for i, parity_list in enumerate(parity_list[::-1]))

    if (error == 0):
        return None, "alınan hamming kodda hata yoktur "
    elif (error >= len(h_copy)):
        return None, "hata tespit edilemiyor "
    else:
        if (h_copy[error - 1] == '0'):
            h_copy[error - 1] = '1'
        elif (h_copy[error - 1] == '1'):
            h_copy[error - 1] = '0'
        h_copy.reverse()
        return error, ''.join(map(str, h_copy))

def generate_hamming_code():
    data_bits = entry_data_bits.get()
    hamming_code = calculate_hamming_code(data_bits)
    messagebox.showinfo(" Üretilen Hamming Kod ", f"Hamming Code: {hamming_code}")

def find_error():
    hamming_code = entry_hamming_code.get()
    error_pos, corrected_code = detect_and_correct_error(hamming_code)
    if error_pos is None:
        messagebox.showinfo("Error Detection", corrected_code)
    else:
        messagebox.showinfo("Error Detection", f"Hata biti : {error_pos}\nHamming Kodun Doğrusu : {corrected_code}")

app = tk.Tk()
app.title("Hamming Code Simulator")

label_intro = tk.Label(app, text="Hamming Code Simulator", font=("Arial", 16), background="yellow")
label_intro.pack(pady=50)

frame_generate = tk.Frame(app, background="blue")
frame_generate.pack(pady=50 )


label_data_bits = tk.Label(frame_generate, text=" Veri Bitlerini Giriniz :")
label_data_bits.pack(side=tk.LEFT)

entry_data_bits = tk.Entry(frame_generate)
entry_data_bits.pack(side=tk.LEFT)

button_generate = tk.Button(frame_generate, text=" Hamming Kod Oluştur  ", command=generate_hamming_code)
button_generate.pack(side=tk.LEFT, padx=10)

frame_find = tk.Frame(app ,background="blue")
frame_find.pack(pady=20)

label_hamming_code = tk.Label(frame_find, text="Hamming Kodu Giriniz:")
label_hamming_code.pack(side=tk.LEFT)

entry_hamming_code = tk.Entry(frame_find)
entry_hamming_code.pack(side=tk.LEFT)

button_find = tk.Button(frame_find, text="Hata bul", command=find_error)
button_find.pack(side=tk.LEFT, padx=10)

app.mainloop()
