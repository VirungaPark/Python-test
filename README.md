## Test-Wannes
You need to develop a web platform to allow users to collect field and farmer data in the DRC. The platform (develop in a Django-like python framework) must allow users to enter information on fields (area, soil type, crop type, etc.) and farmers (name, address, farm size, etc.).

Here are some additional details about the platform requirements:

- Users must be able to login to the platform using a username and password. There should be different levels of access for users depending on their role (Administrator, Data Collector, Agronomists.).
- The collected data must be stored in a standard SQLite database. The data collected must be accessible and exportable via a REST API.
- The platform should also allow users to search and filter data based on different criteria (e.g. field size, crop type, etc.).
- The platform must be developed following good security practices to protect user data. You will need to ensure that passwords are stored securely and that the platform is protected against CSRF and XSS attacks.

In terms of views we can imagine the following structure:

- Views:
   - Homepage: platform overview and login form.
   - Administrator dashboard: allows administrators to manage users and access all collected data.
   - Data collection form: allows data collectors to enter information about farmers and fields.
   - Data search and filtering view: allows users to search and filter collected data.

Below you can find an example of the forms and flow we use to collect data in the field:
[Virunga-test.pptx](https://github.com/VirungaPark/Python-test/files/11365106/Virunga-test.pptx)

Everything must be deployed on an AWS EC2 instance and accessible on a public URL. You can reuse an existing project, you don't have to go into the details at the granular level, the whole thing is to show that you manage to create the technical structure for the accomplishment of such a project.
The final project needs to be pushed on this repo, along with the ec2 url (no need of a domain) plus test credentials example.

For Virunga Foundation
