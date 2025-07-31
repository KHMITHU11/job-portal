// Custom JavaScript for JobPortal

document.addEventListener('DOMContentLoaded', function () {

    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Auto-hide alerts after 5 seconds
    setTimeout(function () {
        var alerts = document.querySelectorAll('.alert');
        alerts.forEach(function (alert) {
            var bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);

    // Form validation enhancement
    var forms = document.querySelectorAll('.needs-validation');
    Array.prototype.slice.call(forms).forEach(function (form) {
        form.addEventListener('submit', function (event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

    // File upload preview
    var fileInputs = document.querySelectorAll('input[type="file"]');
    fileInputs.forEach(function (input) {
        input.addEventListener('change', function () {
            var file = this.files[0];
            var fileName = file ? file.name : 'No file chosen';
            var label = this.nextElementSibling;
            if (label && label.tagName === 'LABEL') {
                label.textContent = fileName;
            }
        });
    });

    // Search form enhancement
    var searchForm = document.querySelector('form[action*="job_list"]');
    if (searchForm) {
        var searchInput = searchForm.querySelector('input[name="query"]');
        var searchButton = searchForm.querySelector('button[type="submit"]');

        if (searchInput && searchButton) {
            // Add loading state to search button
            searchForm.addEventListener('submit', function () {
                searchButton.innerHTML = '<span class="loading"></span> Searching...';
                searchButton.disabled = true;
            });
        }
    }

    // Job card hover effects
    var jobCards = document.querySelectorAll('.job-card');
    jobCards.forEach(function (card) {
        card.addEventListener('mouseenter', function () {
            this.style.transform = 'translateY(-5px)';
        });

        card.addEventListener('mouseleave', function () {
            this.style.transform = 'translateY(0)';
        });
    });

    // Application status badges
    var statusBadges = document.querySelectorAll('.badge');
    statusBadges.forEach(function (badge) {
        if (badge.textContent.includes('Pending')) {
            badge.classList.add('bg-warning');
        } else if (badge.textContent.includes('Shortlisted') || badge.textContent.includes('Accepted')) {
            badge.classList.add('bg-success');
        } else if (badge.textContent.includes('Rejected')) {
            badge.classList.add('bg-danger');
        } else if (badge.textContent.includes('Reviewed')) {
            badge.classList.add('bg-info');
        }
    });

    // Dashboard statistics animation
    var statNumbers = document.querySelectorAll('.stats-card h3');
    statNumbers.forEach(function (stat) {
        var finalNumber = parseInt(stat.textContent);
        var currentNumber = 0;
        var increment = finalNumber / 50;

        var timer = setInterval(function () {
            currentNumber += increment;
            if (currentNumber >= finalNumber) {
                stat.textContent = finalNumber;
                clearInterval(timer);
            } else {
                stat.textContent = Math.floor(currentNumber);
            }
        }, 30);
    });

    // Mobile menu enhancement
    var navbarToggler = document.querySelector('.navbar-toggler');
    var navbarCollapse = document.querySelector('.navbar-collapse');

    if (navbarToggler && navbarCollapse) {
        // Close mobile menu when clicking on a link
        var navLinks = navbarCollapse.querySelectorAll('.nav-link');
        navLinks.forEach(function (link) {
            link.addEventListener('click', function () {
                if (window.innerWidth < 992) {
                    navbarCollapse.classList.remove('show');
                }
            });
        });
    }

    // Back to top button
    var backToTopButton = document.createElement('button');
    backToTopButton.innerHTML = '<i class="fas fa-arrow-up"></i>';
    backToTopButton.className = 'btn btn-primary position-fixed';
    backToTopButton.style.cssText = 'bottom: 20px; right: 20px; z-index: 1000; border-radius: 50%; width: 50px; height: 50px; display: none;';
    document.body.appendChild(backToTopButton);

    window.addEventListener('scroll', function () {
        if (window.pageYOffset > 300) {
            backToTopButton.style.display = 'block';
        } else {
            backToTopButton.style.display = 'none';
        }
    });

    backToTopButton.addEventListener('click', function () {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // Confirmation dialogs
    var deleteButtons = document.querySelectorAll('a[href*="delete"]');
    deleteButtons.forEach(function (button) {
        button.addEventListener('click', function (e) {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
            }
        });
    });

    // Password strength indicator
    var passwordInputs = document.querySelectorAll('input[type="password"]');
    passwordInputs.forEach(function (input) {
        input.addEventListener('input', function () {
            var password = this.value;
            var strength = 0;

            if (password.length >= 8) strength++;
            if (password.match(/[a-z]/)) strength++;
            if (password.match(/[A-Z]/)) strength++;
            if (password.match(/[0-9]/)) strength++;
            if (password.match(/[^a-zA-Z0-9]/)) strength++;

            // Remove existing strength indicator
            var existingIndicator = this.parentNode.querySelector('.password-strength');
            if (existingIndicator) {
                existingIndicator.remove();
            }

            // Create new strength indicator
            var indicator = document.createElement('div');
            indicator.className = 'password-strength mt-2';

            var strengthText = '';
            var strengthClass = '';

            switch (strength) {
                case 0:
                case 1:
                    strengthText = 'Very Weak';
                    strengthClass = 'text-danger';
                    break;
                case 2:
                    strengthText = 'Weak';
                    strengthClass = 'text-warning';
                    break;
                case 3:
                    strengthText = 'Medium';
                    strengthClass = 'text-info';
                    break;
                case 4:
                    strengthText = 'Strong';
                    strengthClass = 'text-success';
                    break;
                case 5:
                    strengthText = 'Very Strong';
                    strengthClass = 'text-success';
                    break;
            }

            indicator.innerHTML = `<small class="${strengthClass}">Password strength: ${strengthText}</small>`;
            this.parentNode.appendChild(indicator);
        });
    });

    // Auto-resize textareas
    var textareas = document.querySelectorAll('textarea');
    textareas.forEach(function (textarea) {
        textarea.addEventListener('input', function () {
            this.style.height = 'auto';
            this.style.height = this.scrollHeight + 'px';
        });
    });

    console.log('JobPortal custom JavaScript loaded successfully!');
}); 