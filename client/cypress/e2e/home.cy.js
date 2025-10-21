describe('Home Page', () => {
  it('loads successfully', () => {
    cy.visit('/');
    cy.contains('Fake Personal Data Generator');
  });

  // it('clicks a button and checks result', () => {
  //   cy.visit('/');
  //   cy.get('button#submit').click();
  //   cy.contains('Submitted!');
  // });
});