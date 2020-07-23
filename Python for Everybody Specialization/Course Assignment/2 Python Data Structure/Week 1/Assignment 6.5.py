text = "X-DSPAM-Confidence:    0.8475";
length = len(text)
f = text.find('0')
print(float(text[f:length]))