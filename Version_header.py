"""
-------------------------------------------------------------------------------------
                              ISTANBUL TECHNICAL UNIVERSITY
                                          MARIN NL

                                        RESTRICTED
-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------
Version      : v0.0.2.404
Author       : Mehmet Alperen BAKICI, Mustafa UNVER, Yasin ERTAS, Siyami Gurkan KUZUCU,
Release Date : 07.06.2023 02:45
Branch Name  : Model_And_Hyperparameters_Changes
-------------------------------------------------------------------------------------
Notes:
    Changing hyperparameters. Learning rates are changed:
    OLD --> NEW :
    LR_ACTOR    1e-3  --> 1e-5
    LR_CRITIC   1e-2  --> 1e-4

    Hyperparameters
    BUFFER_SIZE = int(1e5)  # replay buffer size
    BATCH_SIZE = 128        # minibatch size
    GAMMA = 0.99            # discount factor
    TAU = 1e-3              # for soft update of target parameters
    LR_ACTOR = 1e-5         # learning rate of the actor
    LR_CRITIC = 1e-4        # learning rate of the critic
    WEIGHT_DECAY = 0        # L2 weight decay
--------------------------------------------------------------------------------

-------------------------------------------------------------------------------------
Version      : v0.0.2.403
Author       : Mehmet Alperen BAKICI, Mustafa UNVER, Yasin ERTAS, Siyami Gurkan KUZUCU,
Release Date : 07.06.2023 02:25
Branch Name  : Model_And_Hyperparameters_Changes
-------------------------------------------------------------------------------------
Notes:
    Changing hyperparameters. Buffer size and batch size changes:
    OLD --> NEW :
    BUFFER_SIZE 1e6   --> 1e5
    BATCH_SIZE  256   --> 128
    LR_ACTOR    1e-5  --> 1e-3
    LR_CRITIC   1e-4  --> 1e-2

    Hyperparameters
    BUFFER_SIZE = int(1e5)  # replay buffer size
    BATCH_SIZE = 128        # minibatch size
    GAMMA = 0.99            # discount factor
    TAU = 1e-3              # for soft update of target parameters
    LR_ACTOR = 1e-3         # learning rate of the actor
    LR_CRITIC = 1e-2        # learning rate of the critic
    WEIGHT_DECAY = 0        # L2 weight decay
--------------------------------------------------------------------------------

-------------------------------------------------------------------------------------
Version      : v0.0.2.402
Author       : Mehmet Alperen BAKICI, Mustafa UNVER, Yasin ERTAS, Siyami Gurkan KUZUCU,
Release Date : 06.06.2023 01:00
Branch Name  : Model_And_Hyperparameters_Changes
-------------------------------------------------------------------------------------
Notes:
    Adding new layer to the model.py
    Note: Actor  has 4th hidden layer,
          Critic has 3th hidden layer.
--------------------------------------------------------------------------------

-------------------------------------------------------------------------------------
Version      : v0.0.2.401
Author       : Mehmet Alperen BAKICI
Release Date : 06.06.2023 23:50
Branch Name  : Model_And_Hyperparameters_Changes
-------------------------------------------------------------------------------------
Notes:
    Adding new layer to the model.py
    Note: When adding a new layer this creates a good results than others.
--------------------------------------------------------------------------------

-------------------------------------------------------------------------------------
Version      : v0.0.2.400
Author       : Mehmet Alperen BAKICI
Release Date : 03.06.2023 23:5
Branch Name  : Model_And_Hyperparameters_Changes
-------------------------------------------------------------------------------------
Notes:
    Creating new branch to work every python file.
    State_size chganged 11 to 9. because Our lecturer wants to 9 state_Size for the
    project purpose
--------------------------------------------------------------------------------

-------------------------------------------------------------------------------------
Version      : v0.0.2
Author       : Mehmet Alperen BAKICI
Release Date : 03.06.2023 01:10
Branch Name  : Main
-------------------------------------------------------------------------------------
Notes: 
    Merge 'DDPG Integration' branch into 'Main' branch
--------------------------------------------------------------------------------

-------------------------------------------------------------------------------------
Version      : v0.0.1.201
Author       : Mehmet Alperen BAKICI
Release Date : 03.06.2023
Branch Name  : DDPG_Entegrasyonu
-------------------------------------------------------------------------------------
Notes: 
    Yasin's working files was added. These files updated new versions.
    * DDPG.ipynb
    * VerySimpleAuv.py
-------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------
Version      : v0.0.1.200
Author       : Mehmet Alperen BAKICI
Release Date : 03.06.2023
Branch Name  : DDPG_Entegrasyonu
-------------------------------------------------------------------------------------
Notes: 
    This is DDPG integration branch and its first upload commit.
-------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------
Version      : v0.0.1
Author       : Mehmet Alperen BAKICI
Release Date : 03.06.2023
-------------------------------------------------------------------------------------
Notes: 
    This is the first upload for the Autonomous Undervehicle Project on GitHub Repo
-------------------------------------------------------------------------------------
"""

