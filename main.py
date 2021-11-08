class Animal:
  def __init__(bird,species, name, age, action):
    bird.species=species
    bird.name=name
    bird.age=age
    bird.action=action

  def itsAction(bird):
   print("A "+bird.species+" named as " + bird.name+ " who is " + bird.age + " just " + bird.action)
bird1=Animal("Cat", "Johnny","5","be happy")
bird1.itsAction()