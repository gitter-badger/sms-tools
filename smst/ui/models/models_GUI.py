from Tkinter import *

from ..notebook import Notebook  # window with tabs
from .dftModel_GUI_frame import DftModelFrame
from .stftModel_GUI_frame import StftModelFrame
from .sineModel_GUI_frame import SineModelFrame
from .harmonicModel_GUI_frame import HarmonicModelFrame
from .stochasticModel_GUI_frame import StochasticModelFrame
from .sprModel_GUI_frame import SprModelFrame
from .spsModel_GUI_frame import SpsModelFrame
from .hprModel_GUI_frame import HprModelFrame
from .hpsModel_GUI_frame import HpsModelFrame


def main():
    root = Tk()
    root.title('sms-tools models GUI')
    nb = Notebook(root, TOP)  # make a few diverse frames (panels), each using the NB as 'master':

    # uses the notebook's frame
    f1 = Frame(nb())
    dft = DftModelFrame(f1)

    f2 = Frame(nb())
    stft = StftModelFrame(f2)

    f3 = Frame(nb())
    sine = SineModelFrame(f3)

    f4 = Frame(nb())
    harmonic = HarmonicModelFrame(f4)

    f5 = Frame(nb())
    stochastic = StochasticModelFrame(f5)

    f6 = Frame(nb())
    spr = SprModelFrame(f6)

    f7 = Frame(nb())
    sps = SpsModelFrame(f7)

    f8 = Frame(nb())
    hpr = HprModelFrame(f8)

    f9 = Frame(nb())
    hps = HpsModelFrame(f9)

    nb.add_screen(f1, "DFT")
    nb.add_screen(f2, "STFT")
    nb.add_screen(f3, "Sine")
    nb.add_screen(f4, "Harmonic")
    nb.add_screen(f5, "Stochastic")
    nb.add_screen(f6, "SPR")
    nb.add_screen(f7, "SPS")
    nb.add_screen(f8, "HPR")
    nb.add_screen(f9, "HPS")

    nb.display(f1)

    root.geometry('+0+0')
    root.mainloop()


if __name__ == '__main__':
    main()
