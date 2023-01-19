describe('Tugas Day 18', () => {
    it('Successfull Login', () => {
        cy.visit('https://the-internet.herokuapp.com/login')
        cy.get('#username').type('tomsmith')
        cy.get('#password').type('SuperSecretPassword!')
        cy.get('.fa').click()
        cy.url().should('include', 'https://the-internet.herokuapp.com/secure')

    })
    it('Failed Login Invalid Username', () => {
        cy.visit('https://the-internet.herokuapp.com/login')
        cy.get('#username').type('YantoBasna')
        cy.get('#password').type('SuperSecretPassword!')
        cy.get('.fa').click()

    })
})