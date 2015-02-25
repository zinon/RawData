from BaseSelector import BaseSelector
import ParticleBase
from copy import copy

class ParticleSelector(BaseSelector):
  def __init__(self):
    BaseSelector.__init__(self)
    self.particles = []

  def remove_overlap( self, particles, dR ):
    ParticleBase.remove_overlap( self.particles, particles, dR )

  def clear_particles(self):
    self.particles = []

  def add_particle( self, p ):
    self.particles.append( p )

  def sort_particles(self):
    self.particles.sort()

  def get_particles(self):
    return copy(self.particles)

