signal=None
f_max = 0


import numpy as np


#-------------------------------------- Fourier/Inverse ------------------------------------------#
def fourier(signal):
    """
        Calculate fourier transform of the signal
        Parameters
        ----------
        signal : array of float
            signal points
        Return
        ----------
        f : array of complex
            fourier transform of the signal
    """
    n_samples = len(signal)
    f_hat = np.fft.fft(signal, n_samples)
    l = (len(f_hat)-2)//2
    f = f_hat[:l]
    return f


def inverse_fourier(frequency_list):
    """
        Calculate inverse fourier transform of the signal
        Parameters
        ----------
        frequency_list : array of float
            fourier transform of the signal
        Return
        ----------
        ifft : array of float
            inverse fourier transform of the signal
    """
    return np.fft.ifft(frequency_list)


#------------------------------------------ Time ----------------------------------------------#
def get_time(scale, sr):
    """
        Calculate the time of the signal using sampling rate
        Parameters
        ----------
        scale : array of float
            magnitude of the signal at each point
        sr : int
            number of sampling points per second
        Return
        ----------
        signal_time : array of float 
            time of the sampled signal
    """
    return np.arange(0, len(scale)/sr, 1/sr)

    
def getindex(freq_Hz):

    return freq_Hz/f_max * len(signal)

def split_arrhythmia(ecg_freq):
    """
        separate arithmia components
        Parameters
        ----------
        ecg_freq : array of complex
            arrithmia and normal components 
        Return
        ----------
        f_arrhythmia : array of complex 
        f_normal : array of complex 
    """
    artial_trachycardia = [0]*len(ecg_freq)
    artial_flutter = [0]*len(ecg_freq)
    artial_fibrillation = [0]*len(ecg_freq)

    trachycardia = getindex(250)

    flutter = getindex(350)

    fibrillation = getindex(600)

    # 230
    artial_trachycardia[trachycardia-50:trachycardia+50] = ecg_freq[trachycardia-50:trachycardia+50]*np.hanning(100)
    # 300
    artial_flutter[flutter-50:flutter+50] = ecg_freq[flutter-50:flutter+50]*np.hanning(350-250)
    # 350
    artial_fibrillation[fibrillation-50:fibrillation+50] = ecg_freq[fibrillation-50:fibrillation+50]*np.hanning(360-350)

    f_normal = ecg_freq-artial_trachycardia-artial_flutter-artial_fibrillation

    return artial_trachycardia, artial_flutter, artial_fibrillation, f_normal



def split_music(music_freq, sliders):
    """
        separate music instruments
        Parameters
        ----------
        music_freq : array of complex
            array of music frequencies
        Return
        ----------
        f_piano : array of complex 
        f_guitar : array of complex 
        f_drums : array of complex 
        f_rest : array of complex 
    """

    piano_f1 = getindex(660)
    piano_f2 = getindex(1720)

    guitar_f3 = getindex(294)
    guitar_f3 = getindex(2637)

    drums_f1 = getindex(432)
    drums_f2 = getindex(40)

    f_piano = [0]*len(music_freq)
    f_guitar = [0]*len(music_freq)
    f_drums = [0]*len(music_freq)
    f_rest = [0]*len(music_freq)


    f_piano[piano_f1-1500: piano_f1+1500] = music_freq[piano_f1: piano_f1]*np.hanning(3000)
    f_piano[piano_f2-1500: piano_f2+1500] = music_freq[piano_f2: piano_f2]*np.hanning(3000)
    f_guitar[guitar_f3-1500: guitar_f3+1500] = music_freq[guitar_f3: guitar_f3]*np.hanning(3000)
    f_drums[drums_f1-1500: drums_f2+1500] = music_freq[drums_f1: drums_f1]*np.hanning(3000)

    f_rest = music_freq - f_piano - f_guitar
    return int(sliders["slider0"]["value"])*inverse_fourier(f_piano).real + int(sliders["slider1"]["value"])*inverse_fourier(f_guitar).real + int(sliders["slider2"]["value"])*inverse_fourier(f_drums).real + int(sliders["slider3"]["value"])*inverse_fourier(f_rest).real






def split_vowels(audio_freq):
    """
        separate audio vowels
        Parameters
        ----------
        audio_freq : array of complex
            array of Audio frequencies
        Return
        ----------
        f_A : Vowel A components
        f_Y : Vowel Y components
        f_V : Vowel V components
        f_th : Vowel Th components
        f_ch : Vowel Ch components
        f_s : Vowel S components
        f_o : Vowel O components
        f_r : Vowel R components
        f_n : Vowel N components
        f_d : Vowel D components
        f_rest : Vowel the other components
    """

# inizialization of components arrays
    f_A = [0]*len(audio_freq)
    f_Y = [0]*len(audio_freq)
    f_V = [0]*len(audio_freq)
    f_th = [0]*len(audio_freq)
    f_ch = [0]*len(audio_freq)
    f_s = [0]*len(audio_freq)
    f_o = [0]*len(audio_freq)
    f_r = [0]*len(audio_freq)
    f_n = [0]*len(audio_freq)
    f_d = [0]*len(audio_freq)



    A_f1=getindex(660)
    A_f2=getindex(1720)
    A_f3=getindex(2410)

    Y_f1=getindex(270)
    Y_f2=getindex(2290)
    Y_f3=getindex(3010)

    th_f1=getindex(490)
    th_f2=getindex(1350)

    v_f1=getindex(530)
    v_f2=getindex(1840)

    ch_f1=getindex(600)
    ch_f2=getindex(1170)


    s_f1=getindex(500)
    s_f2=getindex(700)

    o_f1=getindex(730)
    o_f2=getindex(1090)

    r_f1=getindex(640)
    r_f2=getindex(1310)

    n_f1=getindex(44)
    n_f2=getindex(120)
    n_f3=getindex(550)

    d_f1=getindex(55)
    d_f2=getindex(320)
    d_f3=getindex(740)




    # A
    f_A[A_f1-500:A_f1+500] = audio_freq[A_f1-500:A_f1+500] *np.hanning(1000)
    f_A[A_f2-500:A_f2+500]  = audio_freq[A_f2-500:A_f2+500] *np.hanning(1000)
    f_A[A_f3-500:A_f3+500]  = audio_freq[A_f3-500:A_f3+500] *np.hanning(1000)

    # Y
    f_Y[Y_f1-1500:Y_f1+1500] = audio_freq[Y_f1-1500:Y_f1+1500]*np.hanning(3000)
    f_Y[Y_f2-1500:Y_f2+1500] = audio_freq[Y_f2-1500:Y_f2+1500]*np.hanning(3000)
    f_Y[Y_f3-1500:Y_f3+1500] = audio_freq[Y_f3-1500:Y_f3+1500]*np.hanning(3000)

    # V
    f_V[v_f1-1500:v_f1+1500] = audio_freq[v_f1-1500:v_f1+1500]*np.hanning(3000)
    f_V[v_f2-1500:v_f2+1500] = audio_freq[v_f2-1500:v_f2+1500]*np.hanning(3000)

    # Th
    f_th[th_f1-1500:th_f1+1500] = audio_freq[th_f1-1500:th_f1+1500]*np.hanning(3000)

    # Ch
    f_ch[ch_f1-1500:ch_f1+1500] = audio_freq[ch_f1-1500:ch_f1+1500]*np.hanning(3000)

    # S
    f_s[s_f1-1500:s_f1+1500]= audio_freq[s_f1-1500:s_f1+1500]*np.hanning(3000)
    f_s[s_f2-1500:s_f2+1500] = audio_freq[s_f2-1500:s_f2+1500]*np.hanning(3000)

    # O
    f_o[o_f1-1500:o_f1+1500] = audio_freq[o_f1-1500:o_f1+1500]*np.hanning(3000)
    f_o[o_f2-1500:o_f2+1500] = audio_freq[o_f2-1500:o_f2+1500]*np.hanning(3000)

    # R
    f_r[r_f1-1500:r_f1+1500] = audio_freq[r_f1-1500:r_f1+1500]*np.hanning(3000)
    f_r[r_f2-1500:r_f2+1500] = audio_freq[r_f2-1500:r_f2+1500]*np.hanning(3000)

    # N
    f_n[n_f1-1500:n_f1+1500] = audio_freq[n_f1-1500:n_f1+1500]*np.hanning(3000)
    f_n[n_f2-1500:n_f2+1500] = audio_freq[n_f2-1500:n_f2+1500]*np.hanning(3000)
    f_n[n_f3-1500:n_f3+1500] = audio_freq[n_f3-1500:n_f3+1500]*np.hanning(3000)

    # D
    f_d[d_f1-1500:d_f1+1500] = audio_freq[d_f1-1500:d_f1+1500]*np.hanning(3000)
    f_d[d_f2-1500:d_f2+1500] = audio_freq[d_f2-1500:d_f2+1500]*np.hanning(3000)
    f_d[d_f3-1500:d_f3+1500] = audio_freq[d_f3-1500:d_f3+1500]*np.hanning(3000)

    f_rest = audio_freq - f_r - f_A - f_ch - f_d - \
        f_n - f_Y - f_th - f_o - f_n - f_s - f_V
    return np.add(f_A,  np.add(f_Y, np.add(f_V, np.add(f_th, np.add(f_ch, np.add(f_s, np.add(f_o, np.add(f_r, np.add(f_n, np.add(f_d, f_rest))))))))))