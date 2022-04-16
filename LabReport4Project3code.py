import unittest 
import oxo_dialog_ui
import oxo_logic

class TestOxo(unittest.TestCase):
    def testStartGame(self):
        self.assertEqual(oxo_dialog_ui.startGame(), list(" "*9))


    def testResumeGame(self):
        self.assertEqual(oxo_dialog_ui.resumeGame(), oxo_logic.restoreGame())


    def testQuitGame(self):
        self.assertRaises(SystemExit, oxo_dialog_ui.quit)

if __name__=='__main__':
    unittest.main()
