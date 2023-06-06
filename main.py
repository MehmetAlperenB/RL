import gym
import random

import numpy as np
import verySimpleAuv as auv
from collections import deque
import matplotlib.pyplot as plt
import resources
from ddpg_agent import Agent
import torch
env_kwargs = {
        # Set to zero to disable the flow - much faster training.
        "currentVelScale": 1.,
        "currentTurbScale": 2.,
        # Use noise in coefficients for training only.
        "noiseMagActuation": 0.1,
        "noiseMagCoeffs": 0.1,
    }
env = auv.AuvEnv(**env_kwargs)
agent = Agent(state_size=9, action_size=3, random_seed=2)


def ddpg(n_episodes=400, max_t=100, print_every=100):
    scores_deque = deque(maxlen=print_every)
    scores = []
    for i_episode in range(1, n_episodes + 1):
        state = env.reset()
        # print("state: ", state )
        agent.reset()
        score = 0
        for t in range(max_t):
            action = agent.act(state)
            next_state, reward, done, _ = env.step(action)
            agent.step(state, action, reward, next_state, done)
            state = next_state
            score += reward
            if done:
                break
        scores_deque.append(score)
        scores.append(score)
        # print('\rEpisode {}\tAverage Score: {:.2f}'.format(i_episode, np.mean(scores_deque)), end="")
        torch.save(agent.actor_local.state_dict(), 'checkpoint_actor.pth')
        torch.save(agent.critic_local.state_dict(), 'checkpoint_critic.pth')
        if i_episode % print_every == 0:
            print('\rEpisode {}\tAverage Score: {:.2f}'.format(i_episode, np.mean(scores_deque)))

    return scores


scores = ddpg()

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(np.arange(1, len(scores) + 1), scores)
plt.ylabel('Score')
plt.xlabel('Episode #')
plt.show()


agent.actor_local.load_state_dict(torch.load('checkpoint_actor.pth'))
agent.critic_local.load_state_dict(torch.load('checkpoint_critic.pth'))

state = env.reset()
for t in range(200):
    action = agent.act(state, add_noise=False)
    #env.render()
    state, reward, done, _ = env.step(action)
    if done:
        break

env.close()

import resources

# Plot detailed time histories of state, action, etc.
resources.plotDetail(env, labels=["Simple control"])

# Plot an animated replay of the time history.
resources.animateEpisode(env, "test")