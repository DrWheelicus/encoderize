# Security Policy

## Supported Versions

I release patches for security vulnerabilities in the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 0.2.x   | :white_check_mark: |
| < 0.2   | :x:                |

## Reporting a Vulnerability

I take the security of Encoderize seriously. If you believe you have found a security vulnerability, please report it as described below.

### How to Report

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via email to:

**[haydenpmac@gmail.com](mailto:haydenpmac@gmail.com)**

Include the following information in your report:

- Type of vulnerability (e.g., code injection, path traversal, arbitrary file write)
- Full paths of source file(s) related to the manifestation of the vulnerability
- The location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the vulnerability, including how an attacker might exploit it

### What to Expect

After you submit a report, you should expect:

- **Acknowledgment within 48 hours**: I'll confirm receipt of your vulnerability report
- **Regular updates**: I'll keep you informed about my progress
- **Timeline**: I aim to resolve critical vulnerabilities within 7 days
- **Credit**: I'll acknowledge your responsible disclosure in the fix announcement (unless you prefer to remain anonymous)

## Security Best Practices

### For Users

When using Encoderize, please follow these security best practices:

1. **Validate Input**: Always validate and sanitize text input before passing it to Encoderize functions
2. **File Permissions**: Be mindful of output directory permissions when generating SVG files
3. **Dependency Management**: Keep Encoderize and its dependencies up to date:
   ```bash
   pip install --upgrade encoderize
   ```
4. **Ghostscript Security**: Keep Ghostscript updated, as it's a critical dependency for barcode generation

### For Contributors

If you're contributing to Encoderize:

1. **Code Review**: All code changes are reviewed before merging
2. **Dependency Updates**: Report any outdated dependencies with known vulnerabilities
3. **Input Validation**: Ensure all user input is properly validated and sanitized
4. **Path Traversal**: Verify that file operations prevent directory traversal attacks
5. **Testing**: Write security tests for any input handling or file operations

## Known Security Considerations

### File System Operations

Encoderize writes SVG files to disk. Users should:

- Ensure output directories have appropriate permissions
- Be cautious when specifying output paths
- Validate that generated files are placed in expected locations

### Ghostscript Dependency

The `code128_barcode` generator requires Ghostscript, which has had security vulnerabilities in the past:

- Always use the latest version of Ghostscript
- Be aware that barcode generation executes external Ghostscript processes
- Consider security implications in server environments

### Input Sanitization

While Encoderize primarily generates visual representations and doesn't execute code:

- Long input strings may cause performance issues
- Special characters are processed but should be validated by applications
- SVG output should be treated as user-generated content if serving on web applications

## Security Update Process

When a security vulnerability is confirmed:

1. **Private Fix**: I'll develop a fix in a private repository
2. **Testing**: The fix will be thoroughly tested
3. **Release**: A new version will be released with the security fix
4. **Notification**: Security advisories will be published on GitHub
5. **Documentation**: CHANGELOG and release notes will document the fix

## Disclosure Policy

- **Coordinated Disclosure**: I practice coordinated disclosure
- **Public Disclosure**: Security issues will be publicly disclosed after a fix is available
- **Security Advisories**: Critical vulnerabilities will have GitHub Security Advisories created
- **CVE Assignment**: I'll work to obtain CVE identifiers for significant vulnerabilities

## Additional Resources

- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security_warnings.html)
- [OWASP Python Security](https://owasp.org/www-project-python-security/)
- [GitHub Security Advisories](https://github.com/DrWheelicus/encoderize/security/advisories)

## Contact

For security-related questions or concerns, contact:

**Hayden MacIntyre**  
Email: [haydenpmac@gmail.com](mailto:haydenpmac@gmail.com)

---

Thank you for helping keep Encoderize and its users safe!
