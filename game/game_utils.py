
import game.gamestate as gamestate
import game.upgrades as upgrades


def update_player(session, movement, dt):
    session.player.update(movement, dt)
    session.camera.update(session.player.position)

    if session.player.damage_received:
        session.camera.shake(intensity=8, duration=0.2)
        session.player.damage_received = False

    session.camera.update_shake(dt)


def update_world(session, dt):
    session.spawner.update(dt, session)
    session.elapsed_time += dt

    for enemy in session.world.enemies:
        enemy.update(dt, session.player)

        if not enemy.is_alive():
            session.player.add_xp(enemy.xp_reward)

    session.world.enemies = [
        enemy for enemy in session.world.enemies
        if enemy.is_alive()
    ]


def update_weapons(session, dt):
    for weapon in session.player.weapons:
        weapon.update(dt, session.player, session.world)


def update_effects(session, dt):
    for effect in session.world.effects:
        effect.update(dt)

    session.world.effects = [
        effect for effect in session.world.effects
        if effect.is_alive()
    ]


def update_projectiles(session, dt):
    for projectile in session.world.projectiles:
        projectile.update(dt, session.world.enemies)

    session.world.projectiles = [
        projectile for projectile in session.world.projectiles
        if projectile.active
    ]


def update_game_state(session, score_manager):
    if session.player.pending_upgrade > 0:
        session.player.choices.extend(
            upgrades.random_upgrades(session.player)
        )
        return gamestate.GameState.LEVEL_UP

    if not session.player.is_alive():
        score_manager.add_new_score(session.elapsed_time)
        return gamestate.GameState.GAME_OVER

    return gamestate.GameState.PLAYING
