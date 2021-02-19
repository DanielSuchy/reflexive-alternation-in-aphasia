PennController.ResetPrefix(null) // Shorten command names
//PennController.DebugOff() //turn off on deploy!!!
var progressBarText = "postup";  //tímhle se určuje text pod tím progress barem
Sequence( "intro", "form", "prePractice", "practice1", "practice2", "afterPractice", randomize("experiment"), "feedback" , SendResults() , "bye" ) //sekvence jednotlivých "kusů" experimentu (tj. trials), randomize říká, že ty jednotlivé položky v "ostrém" experimentu se mají prezentovat v náhodném pořadí


newTrial("intro",                                                                            
    newHtml("consent", "consent.html")
        .settings.checkboxWarning("Prosím, potvrďte souhlas")  //tady je nastavené, aby se dalo pokračovat jenom po odkliknutí
        .print()
        .log()
    ,
    newButton("continue", "pokračovat")
        .print()
        .wait(
        getHtml("consent").test.complete()
            .failure( getHtml("consent").warn() )
        )
)


newTrial("form",                                                                            //v tomhle trialu se sbírají demografická data
    newHtml("demographics", "demographics.html")
        .settings.radioWarning("Vyplňte prosím všechny požadované údaje.")                  //zase je tady nastavené, aby se dalo pokračovat jenom po vyplnění všech kolonek
        .settings.inputWarning("Vyplňte prosím všechny požadované údaje.")
        .print()
        .log()
    ,
    newButton("continue", "pokračovat")
        .print()
        .wait(
        getHtml("demographics").test.complete()
            .failure( getHtml("demographics").warn() )
        )
)


newTrial("prePractice",                                                         //trial s instrukcemi. ty jsou opět v samostatném html souboru, kde je možné text upravit.
    newHtml("instrukce", "prePractice.html")
        .print()
    ,
    newButton("Zahájit nácvik")
        .print()
        .wait()

)

newTrial("practice1",                //v těchle dvou trialech je nácvik.
    newTimer(500)
        .start()
        .wait()
    ,
    newText("q", "<p>Vrátný zapsal datum do kalendáře.</p>")
        .print()
    ,
    newHtml("<hr>")
        .print()
    ,
    newScale("anoNe", "dává smysl", "nedává smysl", "nejsem si jistá/ý")                                    
        .vertical()
        .css("margin", "10px")
        .print()
        .log()
        .wait()
        .remove()
    ,
    getText("q")
        .remove()
    ,
    newTimer(500)
        .start()
        .wait()
)
    
newTrial("practice2",                //v těchle dvou trialech je nácvik.
    newTimer(500)
        .start()
        .wait()
    ,
    newText("q", "<p>Vrátný se zapsal datum do kalendáře.</p>")
        .print()
    ,
    newHtml("<hr>")
        .print()
    ,
    newScale("anoNe", "dává smysl", "nedává smysl", "nejsem si jistá/ý")                                    
        .vertical()
        .css("margin", "10px")
        .print()
        .log()
        .wait()
        .remove()
    ,
    getText("q")
        .remove()
    ,
    newTimer(500)
        .start()
        .wait()
)

newTrial("afterPractice",                       //text po skončení nácviku. tady by bylo dobré napsat, že následuje experiment, že to bude probíhat úplně stejně a kolik bude celkem položek. je to zase v samostatném html souboru, kde je třeba text upravit
    newHtml("afterPractice.html")
        .print()
    ,
        newButton("Zahájit experiment")
            .print()
            .wait()
)



Template("stimuli.csv", variable =>                             //vlastní experiment je vytvořený tak, že je tady šablona (template), ve které je popsaný průběh jedné položky. jednotlivé položky se pak berou z tabulky "stimuli.csv", která je ve složce resources
  newTrial("experiment",
	newTimer(500)
        .start()
        .wait()
    ,
    newText("q", variable.Sentence)        
        .print()
    ,
    newHtml("<hr>")
        .print()
    ,
    newScale("anoNe", "dává smysl", "nedává smysl", "nejsem si jistá/ý")                                    
        .vertical()
        .css("margin", "10px")
        .print()
        .log()
        .wait()
        .remove()
    ,
	getText("q")
	    .remove()
	,
	newTimer(500)
        .start()
        .wait()
  )
	//tady v těch čtyřech řádkách je nastavené, aby se ve výsledcích ke každé položce kromě vybrané odpovědi a reakčního času zaznamenávaly další údaje z tabulky (to pak bude praktické pro analýzu)
	.log("Item", variable.Item)                 //obsahuje kód položky            
	.log("Answer.correct", variable.Answer)     //obsahuje správnou odpověď na otázku
 )

newTrial("feedback",
    newText("<p>Experiment je u konce. Pokud máte k experimentu nějaký komentář, můžete ho napsat sem.</p><p>Pokud žádný komentář nemáte, nechte pole prázdné a klikněte na <i>odeslat</i>.</p><br>")
        .print()
    ,
    newTextInput("fbk")
        .log()
        .lines(0)
        .size(400, 100)
        .print()
    ,
    newButton("send", "odeslat")
        .print()
        .wait()
) 
 
 
SendResults()               //tímhle příkazem se uloží výsledky celého experimentu.


newTrial( "bye" ,           //tady je koncová obrazovka
    newText("<p>Děkuji Vám za účast. Nyní můžete záložku zavřít.</p>").print(),
    newButton().wait()  // Wait for a click on a non-displayed button = wait here forever
)
.setOption( "countsForProgressBar" , false )