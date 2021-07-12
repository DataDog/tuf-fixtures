# For instructions on using this script, please see the README.

from unittest import mock

from fixtures import (
    TUFTestFixtureSimple,
    TUFTestFixtureAttackRollback,
    TUFTestFixtureDelegated,
    TUFTestFixtureNestedDelegated,
    TUFTestFixtureUnsupportedDelegation,
    TUFTestFixtureNestedDelegatedErrors,
    TUFTestFixtureThresholdTwo,
    TUFTestFixtureThresholdTwoAttack,
    TUFTestFixtureTerminatingDelegation,
    TUFTestFixtureTopLevelTerminating,
    TUFTestFixtureNestedTerminatingNonDelegatingDelegation,
    TUFTestFixture3LevelDelegation,
    PublishedTwice
)


@mock.patch('time.time', mock.MagicMock(return_value=1577836800))
def generate_fixtures():
    TUFTestFixtureSimple.build()
    TUFTestFixtureAttackRollback.build()
    TUFTestFixtureDelegated.build()
    TUFTestFixtureNestedDelegated.build()
    TUFTestFixtureUnsupportedDelegation.build()
    TUFTestFixtureNestedDelegatedErrors.build()
    TUFTestFixtureThresholdTwo.build()
    TUFTestFixtureThresholdTwoAttack.build()
    TUFTestFixtureTerminatingDelegation.build()
    TUFTestFixtureTopLevelTerminating.build()
    TUFTestFixtureNestedTerminatingNonDelegatingDelegation.build()
    TUFTestFixture3LevelDelegation.build()
    PublishedTwice.build()
    PublishedTwice.build(rotate_keys='timestamp')
    PublishedTwice.build(rotate_keys='snapshot')


generate_fixtures()
