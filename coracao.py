import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Fórmulas do coração
t = np.linspace(0, 2 * np.pi, 300)
base_x = 16 * np.sin(t)**3
base_y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# Configuração da figura
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.axis('off')
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

line, = ax.plot([], [], color='red', linewidth=2)

# Parâmetros
draw_frames = len(t)           # Quantos quadros para desenhar o coração
pulse_frames = 60              # Quantos quadros de pulsação (loopável)
total_frames = draw_frames + pulse_frames

# Animação
def animate(i):
    if i < draw_frames:
        # Fase 1: desenhar o coração
        line.set_data(base_x[:i], base_y[:i])
    else:
        # Fase 2: pulsar o coração pronto
        pulse_phase = (i - draw_frames) / pulse_frames * 2 * np.pi
        pulse = 1 + 0.05 * np.sin(3 * pulse_phase)  # pulsação suave
        x = base_x * pulse
        y = base_y * pulse
        line.set_data(x, y)
    return line,

# Criar animação com loop infinito (repeat=True)
anim = FuncAnimation(
    fig,
    animate,
    frames=total_frames,
    interval=30,  # controla a velocidade geral da animação
    blit=True,
    repeat=True
)

# Salvar GIF
writer = PillowWriter(fps=33, metadata={'duration': 30})  # 30ms por quadro
anim.save("coracao.gif", writer=writer)

plt.close()
print("GIF com traçado + pulsação contínua salvo como coracao.gif")
