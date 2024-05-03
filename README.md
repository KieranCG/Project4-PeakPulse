# PeakPulse

## Project Introduction
This project is a the final project for my Code Institute learning programe. It is predominately designed to showcase a website built using Django and deployed to Heroku.

To view the deployed website click [here]

### User Story

1. **As a fitness enthusiast, I want to browse and purchase gym equipment online, so I can conveniently access high-quality gear for my workouts.**

2. **As a user, I want to access a database of exercises categorized by muscle group and equipment, so I can discover new workouts and plan my fitness routines effectively.**

3. **As a fitness enthusiast, I want to log my own exercises and workouts, so I can track my progress and stay motivated to achieve my fitness goals.**

4. **As a community member, I want to engage with other users by leaving posts on a community wall, so I can share my fitness journey, ask questions, and provide support to fellow members.**

5. **As a user, I want to leave testimonials about my experience with PeakPulse, so I can share my satisfaction with the platform and encourage others to join the community.**

## About the Development Cycle

### Planning

- **Objective**: Create a website platform that meets the needs of gym enthusiasts and home sportspeople.
- **Activities**:
  - Define the core features and functionality of the app, such as webstore, search, and user profiles.
  - Identify the target audience, including gym enthusiasts, home sportspeople, and diet users.

### Requirements Gathering

- **Objective:** Identify detailed requirements to inform the design and development process.
- **Activities:**
  - Define user stories and personas to understand user needs and expectations.
  - Identify technical requirements, including platform compatibility and data storage options.

1. **Technologies Used**:
   - Django
   - Python 3.x
   - HTML/CSS
   - JavaScript
   - Bootstrap
   - jQuery
   - Git

2. **Development Process**:
   - PeakPulse was developed using an agile development methodology, with iterative cycles of planning, implementation, testing, and deployment.
   - Project management and collaboration were facilitated through GitHub for version control and Slack for communication.
   - Continuous integration and continuous deployment (CI/CD) pipelines were set up to automate testing and deployment processes.

3. **Feature Implementation**:
   - Features such as the online shop, exercise database, and community wall were implemented using Django's built-in functionalities and third-party libraries.
   - Challenges faced during implementation included integrating payment gateways for the online shop and implementing real-time updates for the community wall.

4. **Testing and Quality Assurance**:
   - Integration testing was performed to validate interactions between different modules and functionalities.
   - Static code analysis tools such as pylint and flake8 were used to maintain code quality and adherence to coding standards.

5. **Feedback and Iteration**:
   - User feedback was collected through a small group of external testers that feedback to the developer.
   - Iterative updates were made to PeakPulse based on user feedback, including enhancements to the user interface, performance optimizations, and bug fixes.
   - The project roadmap was continuously refined based on user needs.

6. **Future Development Plans**:
   - Future development plans for PeakPulse include implementing social media integration for user authentication, enhancing the recommendation engine for personalized workout suggestions, and expanding the product catalog in the online shop.
   - Community contributions and suggestions for new features are welcomed and encouraged to further enrich the PeakPulse platform.

## Data Models

### Exercise Models

#### Exercise Category

- Represents categories of exercises.
- Attributes:
  - `name`: Name of the category.
  - `friendly_name`: Friendly name for display purposes.

#### Exercise

- Represents individual exercises logged by users.
- Attributes:
  - `user`: ForeignKey to link each exercise with a user.
  - `title`: Title of the exercise.
  - `description`: Description of the exercise.
  - `bodypart`: Body part targeted by the exercise.
  - `equipment`: Equipment required for the exercise.
  - `level`: Difficulty level of the exercise.
  - `rating`: Rating of the exercise.
  - `ratingdesc`: Description of the exercise rating.
  - `category`: ForeignKey to link each exercise with an ExerciseCategory.
  - Additional Fields:
    - `sets`: Number of sets performed.
    - `repetitions`: Number of repetitions per set.
    - `duration`: Duration of the exercise.
    - `weight`: Weight used for the exercise.
    - `distance`: Distance covered during the exercise.
    - `intensity`: Intensity level or heart rate.
    - `notes`: Additional notes or comments.

#### Exercise Log

- Represents logs of exercises performed by users.
- Attributes:
  - `user`: ForeignKey to link each log with a user.
  - `exercise`: ForeignKey to link each log with an Exercise.
  - `date`: Date of the exercise log.
  - `sets`: Number of sets performed.
  - `repetitions`: Number of repetitions per set.
  - `duration`: Duration of the exercise.
  - `weight`: Weight used for the exercise.
  - `distance`: Distance covered during the exercise.
  - `intensity`: Intensity level or heart rate.
  - `notes`: Additional notes or comments.

### Product Models

#### Category

- Represents categories of products available in the shop.
- Attributes:
  - `name`: Name of the category.
  - `friendly_name`: Friendly name for display purposes.

#### Product

- Represents individual products available for purchase.
- Attributes:
  - `category`: ForeignKey to link each product with a Category.
  - `sku`: Stock Keeping Unit for the product.
  - `name`: Name of the product.
  - `description`: Description of the product.
  - `has_sizes`: Indicates if the product comes in different sizes.
  - `price`: Price of the product.
  - `rating`: Rating of the product.
  - `image_url`: URL of the product image.
  - `image`: Image file of the product.

### Community Models

#### Post

- Represents posts created by users on the community wall.
- Attributes:
  - `user`: ForeignKey to link each post with a user.
  - `content`: Content of the post.
  - `created_at`: Date and time when the post was created.

#### Comment

- Represents comments left by users on posts.
- Attributes:
  - `user`: ForeignKey to link each comment with a user.
  - `post`: ForeignKey to link each comment with a post.
  - `content`: Content of the comment.
  - `created_at`: Date and time when the comment was created.

#### Testimonial

- Represents testimonials left by users.
- Attributes:
  - `user`: ForeignKey to link each testimonial with a user.
  - `content`: Content of the testimonial.
  - `created_at`: Date and time when the testimonial was created.

### User Profile Model

#### UserProfile

- Represents user profiles containing default delivery information and order history.
- Attributes:
  - `user`: OneToOneField linking each profile with a user.
  - `default_phone_number`: Default phone number for delivery.
  - `default_street_address1`: First line of default street address.
  - `default_street_address2`: Second line of default street address.
  - `default_town_or_city`: Default town or city for delivery.
  - `default_county`: Default county for delivery.
  - `default_postcode`: Default postcode for delivery.
  - `default_country`: Default country for delivery.

### Signals

- `create_or_update_user_profile`: Signal to create or update the user profile when a user is created or updated.

## UI Design

### Design Principles
- The user interface (UI) design for PeakPulse is guided by principles of simplicity, consistency, and usability.
- Our goal is to provide users with an intuitive and visually appealing experience that facilitates their fitness journey.

### Components and Layout
- The UI incorporates common components such as navigation bars, cards, and grids to organize content effectively.
- Screenshots of the website layout demonstrate the arrangement of components on different pages, ensuring a clear and coherent structure.

### Styling and Theming
- PeakPulse features a modern and energetic visual style, with vibrant color schemes and bold typography to reflect its fitness-oriented branding.
- The chosen styling decisions aim to create a motivating and inspiring atmosphere for users as they engage with the platform.

### Responsive Design
- The UI design is responsive, adapting seamlessly to various screen sizes and devices, including desktops, tablets, and mobile phones.
- Techniques such as fluid layouts and media queries ensure that the user experience remains consistent and optimized across different devices.

### Accessibility Considerations
- Accessibility features are integrated into the UI design to ensure that PeakPulse is usable by people with disabilities.
- Compliance with accessibility guidelines and best practices improves inclusivity and ensures a positive experience for all users.

### Interactive Elements
- Interactive elements such as buttons, forms, and animations enhance user engagement and interactivity on the PeakPulse website.
- These elements contribute to a dynamic and engaging experience, encouraging users to interact with the platform and track their fitness progress actively.

### User Feedback and Iteration
- User feedback and usability testing have played a significant role in iterating on the UI design of PeakPulse.
- Changes and improvements based on user input have helped optimize the user experience and address any pain points encountered by users.

### Future Design Enhancements
- In the future, we plan to explore additional design enhancements and features to further enhance the UI of PeakPulse.
- We welcome feedback and suggestions from users and contributors to help shape the evolution of the UI design over time.
