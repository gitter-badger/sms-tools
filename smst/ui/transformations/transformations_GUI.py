from Tkinter import *

from ..notebook import Notebook  # window with tabs
from .stftMorph_GUI_frame import StftMorphFrame
from .sineTransformations_GUI_frame import SineTransformationsFrame
from .harmonicTransformations_GUI_frame import HarmonicTransformationsFrame
from .stochasticTransformations_GUI_frame import StochasticTransformationsFrame
from .hpsTransformations_GUI_frame import HpsTransformationsFrame
from .hpsMorph_GUI_frame import HpsMorphFrame


def main():
    root = Tk()
    root.title('sms-tools transformations GUI')
    nb = Notebook(root, TOP)  # make a few diverse frames (panels), each using the NB as 'master':

    # uses the notebook's frame
    f1 = Frame(nb())
    stft = StftMorphFrame(f1)

    f2 = Frame(nb())
    sine = SineTransformationsFrame(f2)

    f3 = Frame(nb())
    harmonic = HarmonicTransformationsFrame(f3)

    f4 = Frame(nb())
    stochastic = StochasticTransformationsFrame(f4)

    f5 = Frame(nb())
    hps = HpsTransformationsFrame(f5)

    f6 = Frame(nb())
    hpsmorph = HpsMorphFrame(f6)

    nb.add_screen(f1, "STFT Morph")
    nb.add_screen(f2, "Sine")
    nb.add_screen(f3, "Harmonic")
    nb.add_screen(f4, "Stochastic")
    nb.add_screen(f5, "HPS")
    nb.add_screen(f6, "HPS Morph")

    nb.display(f1)

    root.geometry('+0+0')
    root.mainloop()


if __name__ == '__main__':
    main()
