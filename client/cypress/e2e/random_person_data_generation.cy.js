function generatePersonCard({numberOfPersons = 1, partialOption = null, visibleFields = []} = {}) {
  // ARRANGE
  cy.visit('/');

  if (numberOfPersons > 1) {
    cy.get('#txtNumberPersons')
      .should('exist')
      .clear()
      .type(numberOfPersons.toString())
      .should('have.value', numberOfPersons.toString());
  }

  if (partialOption) {
    cy.get('#chkPartialOptions')
      .should('exist')
      .should('not.be.disabled')
      .check()
      .should('be.checked');

    cy.get('#cmbPartialOptions')
      .should('exist')
      .select(partialOption)
      .should('have.value', partialOption);
  }

  // ACT
  cy.get('input[type="submit"][value="Generate"]').click();

  // ASSERT
  cy.get('.personCard', {timeout: 10000}).should('exist');

  // ASSERT correct amount of persons generated
  const personCards = cy.get('.personCard').should('have.length', numberOfPersons);

  personCards.each((card) => {
    cy.wrap(card).within(() => {
      visibleFields.forEach((selector) => {
        cy.get(selector).should('not.be.empty');
      });
    });
  });
}

describe('Person Generator Tests', () => {
  it('generates a single random person', () => {
    generatePersonCard({
      visibleFields: ['.firstNameValue', '.lastNameValue', '.genderValue']
    });
  });

  it('generates 10 random persons', () => {
    generatePersonCard({
      numberOfPersons: 10,
      visibleFields: ['.firstNameValue', '.lastNameValue', '.genderValue']
    });
  });

  it('generates person card with only CPR visible', () => {
    generatePersonCard({
      partialOption: 'cpr',
      visibleFields: ['.cprValue']
    });
  });

  it('generates person card with only name and gender visible', () => {
    generatePersonCard({
      partialOption: 'name-gender',
      visibleFields: ['.firstNameValue', '.lastNameValue', '.genderValue']
    });
  });

  it('generates person card with only name, gender and DOB visible', () => {
    generatePersonCard({
      partialOption: 'name-gender-dob',
      visibleFields: ['.firstNameValue', '.lastNameValue', '.genderValue', '.dobValue']
    });
  });

  it('generates person card with CPR, name and gender visible', () => {
    generatePersonCard({
      partialOption: 'cpr-name-gender',
      visibleFields: ['.cprValue', '.firstNameValue', '.lastNameValue', '.genderValue']
    });
  });

  it('generates person card with CPR, name, gender and DOB visible', () => {
    generatePersonCard({
      partialOption: 'cpr-name-gender-dob',
      visibleFields: ['.cprValue', '.firstNameValue', '.lastNameValue', '.genderValue', '.dobValue']
    });
  });

  it('generates person card with address visible', () => {
    generatePersonCard({
      partialOption: 'address',
      visibleFields: ['.address', '.streetValue', '.townValue',]
    });
  });

  it('generates person card with phone number visible', () => {
    generatePersonCard({
      partialOption: 'phone',
      visibleFields: ['.phoneNumber']
    });
  });
});
