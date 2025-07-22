# Peer Recognition Dashboard

A comprehensive web-based dashboard for tracking and visualizing employee peer recognition across different quarters and departments.

## Features

### 📊 Dashboard Overview
- Real-time statistics display
- Quarter-wise filtering
- Recognition metrics and analytics
- Department-wise breakdown

### 👥 Employee Management
- Complete employee profiles with ID, name, designation, and department
- Quarter-wise recognition tracking
- Achievement badges and recognition counts
- Advanced search and filtering capabilities

### 🏢 Department Analytics
- Department-wise employee distribution
- Recognition statistics per department
- Performance comparison across departments

### 📈 Analytics & Insights
- Quarter-wise recognition trends
- Top-performing departments
- Visual charts and graphs
- Performance metrics

## Files Structure

```
peer-recognition-dashboard/
├── peer-recognition-dashboard.html    # Basic dashboard version
├── advanced-dashboard.html           # Enhanced dashboard with analytics
├── employee-data.json                # Structured employee data
└── README.md                         # This documentation
```

## Quick Start

### Option 1: Basic Dashboard
1. Open `peer-recognition-dashboard.html` in any modern web browser
2. Use the quarter filters to view specific time periods
3. Search for employees using the search box
4. View employee cards with recognition details

### Option 2: Advanced Dashboard
1. Open `advanced-dashboard.html` in any modern web browser
2. Navigate between different tabs:
   - **Dashboard**: Overview and statistics
   - **Employees**: Detailed employee listing with filters
   - **Departments**: Department-wise analytics
   - **Analytics**: Charts and performance insights

## Dashboard Features

### 🎯 Quarter Filtering
- **All Quarters**: View complete yearly data
- **Q1 2024**: January - March focus period
- **Q2 2024**: April - June growth phase
- **Q3 2024**: July - September peak performance
- **Q4 2024**: October - December year-end achievements

### 🔍 Search & Filter
- **Text Search**: Search by employee name, ID, designation, or department
- **Department Filter**: Filter by specific departments
- **Quarter Filter**: Focus on specific quarterly periods

### 📋 Employee Information
Each employee card displays:
- Employee ID and name
- Professional designation
- Department affiliation
- Quarter assignment
- Recognition count
- Achievement badges
- Join date (in advanced version)

### 📊 Statistics
- Total employee count
- Number of departments
- Total recognitions awarded
- Average recognitions per employee

## Data Structure

### Employee Data Fields
```json
{
  "id": "EMP001",
  "name": "Alice Johnson",
  "designation": "Senior Software Engineer",
  "department": "Engineering",
  "quarter": "Q1",
  "recognitions": 5,
  "achievements": ["Code Quality Award", "Team Player"],
  "joinDate": "2023-01-15",
  "email": "alice.johnson@company.com"
}
```

### Supported Departments
- Engineering
- Product
- Design
- Marketing
- Analytics
- Human Resources
- Sales
- Quality Assurance
- Operations
- Security
- Finance

## Customization

### Adding New Employees
1. Edit the `employeeData` array in the HTML file
2. Follow the existing data structure
3. Ensure unique employee IDs
4. Assign appropriate quarters (Q1, Q2, Q3, Q4)

### Modifying Departments
1. Update the department lists in both the data and filter options
2. Ensure consistency across all employee records

### Styling Customization
- Modify the CSS variables for colors and themes
- Adjust grid layouts for different screen sizes
- Customize animations and transitions

## Browser Compatibility

The dashboard is compatible with:
- Chrome 80+
- Firefox 75+
- Safari 13+
- Edge 80+

## Mobile Responsiveness

The dashboard is fully responsive and optimized for:
- Desktop computers (1200px+)
- Tablets (768px - 1199px)
- Mobile phones (320px - 767px)

## Performance Features

- Efficient filtering algorithms
- Responsive grid layouts
- Smooth animations and transitions
- Optimized for large datasets

## Usage Examples

### Quarterly Review
1. Select specific quarter (e.g., Q3 2024)
2. Review recognition statistics
3. Identify top performers
4. Analyze department contributions

### Department Analysis
1. Navigate to Departments tab
2. Compare employee counts across departments
3. Review recognition distributions
4. Identify high-performing teams

### Employee Search
1. Use search box to find specific employees
2. Filter by department or quarter
3. Review individual achievements
4. Track recognition trends

## Future Enhancements

Potential improvements could include:
- Data export functionality
- Integration with HR systems
- Real-time data updates
- Advanced analytics dashboard
- Role-based access control
- Notification systems

## Technical Details

### Technologies Used
- HTML5 for structure
- CSS3 with Flexbox and Grid for responsive design
- Vanilla JavaScript for interactivity
- CSS Custom Properties for theming
- Local data storage using JavaScript arrays

### Performance Optimizations
- Efficient DOM manipulation
- Debounced search functionality
- Optimized CSS animations
- Minimal external dependencies

## Support

For technical support or feature requests, please refer to the documentation or contact the development team.

---

**Note**: This dashboard is designed for demonstration purposes. In a production environment, consider implementing proper data persistence, user authentication, and backend integration.
